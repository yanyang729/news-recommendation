import pickle
import sys
import os
import redis
from bson.json_util import dumps, loads
import json

sys.path.append(os.path.join(os.path.dirname(__file__), '..','common'))
import mongodb_client

BATCH_SIZE = 10
NEWS_TABLE_NAME = 'news'
NEWS_LIMIT = 30
REDIS_HOST = 'localhost'
REDIS_PORT = 6379
USER_NEWS_TTL_IN_SECONDS = 60*10

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

    return loads(dumps(sliced_news)) # TODO: check

