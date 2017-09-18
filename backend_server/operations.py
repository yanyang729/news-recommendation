import pickle
import sys
import os
import redis
from bson.json_util import dumps, loads
import json
from datetime import datetime

sys.path.append(os.path.join(os.path.dirname(__file__), '..','common'))
import mongodb_client
from cloudAMQP_client import CloundAMQPClient as CloudAMQPClient
import news_recommendation_service_client
import json


with open(os.path.join(os.path.dirname(__file__),'..','config','backend_server_config.json')) as f:
    config = json.load(f)['operations']

BATCH_SIZE = config['BATCH_SIZE']
NEWS_TABLE_NAME = config['NEWS_TABLE_NAME']
NEWS_LIMIT = config['NEWS_LIMIT']
REDIS_HOST = config['REDIS_HOST']
REDIS_PORT = config['REDIS_PORT']
USER_NEWS_TTL_IN_SECONDS = config['USER_NEWS_TTL_IN_SECONDS']

CLICK_LOGS_TABLE_NAME = config['CLICK_LOGS_TABLE_NAME']

LOG_CLICKS_TASK_QUEUE_URL = config['LOG_CLICKS_TASK_QUEUE_URL']
LOG_CLICKS_TASK_QUEUE_NAME = config['LOG_CLICKS_TASK_QUEUE_NAME']

cloudAMQP_client = CloudAMQPClient(LOG_CLICKS_TASK_QUEUE_URL, LOG_CLICKS_TASK_QUEUE_NAME)
redis_client = redis.StrictRedis(REDIS_HOST, REDIS_PORT, db=0)


def getNewsSummariesForUser(user_id, page_num):
    page_num = int(page_num)

    begin_index = (page_num - 1) * BATCH_SIZE
    end_index = page_num * BATCH_SIZE

    sliced_news = []

    if redis_client.get(user_id) is not None:
        news_digests = pickle.loads(redis_client.get(user_id))

        sliced_news_digests = news_digests[begin_index:end_index]

        db = mongodb_client.get_db()
        sliced_news = list(db[NEWS_TABLE_NAME].find({'digest':{'$in':sliced_news_digests}}))
    else:
        db = mongodb_client.get_db()
        total_news = list(db[NEWS_TABLE_NAME].find().sort([('publishedAt',-1)]).limit(NEWS_LIMIT))
        total_news_digest = map(lambda x: x['digest'],total_news)

        redis_client.set(user_id, pickle.dumps(total_news_digest))
        redis_client.expire(user_id, USER_NEWS_TTL_IN_SECONDS)

        sliced_news = total_news[begin_index: end_index]


    preference = news_recommendation_service_client.getPreferenceForUser(user_id)
    topPreference = None

    if preference is not None and len(preference) > 0:
        topPreference = preference[0]

    for news in sliced_news:
        del news['text']
        if news['class'] == topPreference:
            news['reason'] = 'Recommend'
        else:
            news['reason'] = news['class']
        if news['publishedAt'].date() == datetime.today().date():
            news['time'] = 'today'

    return json.loads(dumps(sliced_news)) # TODO: check


def logNewsClickForUser(user_id, news_id):
    message = {'userId': user_id, 'newsId': news_id, 'timestamp': datetime.utcnow()}

    db = mongodb_client.get_db()
    db[CLICK_LOGS_TABLE_NAME].insert(message)

    message = {'userId': user_id, 'newsId': news_id, 'timestamp': str(datetime.utcnow())}
    cloudAMQP_client.sendMessage(message)