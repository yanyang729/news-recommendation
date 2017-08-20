import hashlib
import os
import sys
import datetime

sys.path.append(os.path.join(os.path.dirname(__file__),'..','common'))
import news_api_client as client
import redis

NEWS_TIME_OUT_IN_SECONDS = 3600 * 24 * 3

REDIS_HOST = 'localhost'

REDIS_PORT = 6379

NEWS_SOURCES = ['cnn']

redis_client = redis.StrictRedis(REDIS_HOST, REDIS_PORT)



while True:

    news_list = client.getNewsFromSource(NEWS_SOURCES)

    num_of_news = 0

    for news in news_list:
        news_digest = hashlib.md5(news['title'].encode('utf-8').digest().encode('base64'))

        if redis_client.get(news_digest) is None:
            num_of_news += 1
            news['digest'] = news_digest

            if news['publishedAt'] is None:
                news['publishedAt'] = datetime.datetime.utcnow().strftime() #TODO:

            redis_client.set(news_digest, "True")
            redis_client.expire() # TODO