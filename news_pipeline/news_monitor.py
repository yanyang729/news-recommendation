import hashlib
import os
import sys
import datetime
import redis

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
import news_api_client as client
from cloudAMQP_client import CloundAMQPClient as CloudAMQPClient


SLEEP_TIME_IN_SECONDS = 10
NEWS_TIME_OUT_IN_SECONDS = 3600 * 24 * 3

REDIS_HOST = 'localhost'
REDIS_PORT = 6379

SCRAPE_NEWS_TASK_QUEUE_URL = "amqp://holajbod:izGGmsaUFTKfY1gOSSeTN8N466Yi6_1C@crane.rmq.cloudamqp.com/holajbod"
SCRAPE_NEWS_TASK_QUEUE_NAME = "news-task"

NEWS_SOURCES = [
    'bbc-news',
    'bbc-sport',
    'bloomberg',
    'cnn',
    'entertainment-weekly',
    'espn',
    'ign',
    'techcrunch',
    'the-new-york-times',
    'the-wall-street-journal',
    'the-washington-post'
]

redis_client = redis.StrictRedis(REDIS_HOST, REDIS_PORT)
cloudAMQP_client = CloudAMQPClient(SCRAPE_NEWS_TASK_QUEUE_URL, SCRAPE_NEWS_TASK_QUEUE_NAME)

while True:

    news_list = client.getNewsFromSource(NEWS_SOURCES)

    num_of_news = 0

    for news in news_list:
        news_digest = hashlib.md5(news['title'].encode('utf-8')).digest().encode('base64')

        if redis_client.get(news_digest) is None:
            num_of_news += 1
            news['digest'] = news_digest

            if news['publishedAt'] is None:
                news['publishedAt'] = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

            redis_client.set(news_digest, "True")
            redis_client.expire(news_digest, NEWS_TIME_OUT_IN_SECONDS)

            cloudAMQP_client.sendMessage(news)

    print "Fetched %d news." % num_of_news

    cloudAMQP_client.sleep(SLEEP_TIME_IN_SECONDS)