import datetime
import os
import sys

from dateutil import parser
from sklearn.feature_extraction.text import TfidfVectorizer

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'logger'))
import mongodb_client
from cloudAMQP_client import CloundAMQPClient as CloudAMQPClient
import news_topic_modeling_service_client
from log import *

DEDUPE_NEWS_TASK_QUEUE_URL = "amqp://rcsdmawz:QDrDPYaGXyAA0WU8NiVWopTTH3yVkULw@wasp.rmq.cloudamqp.com/rcsdmawz"
DEDUPE_NEWS_TASK_QUEUE_NAME = "news-deduper"


SLEEP_TIME_IN_SECONDS = 1

NEWS_TABLE_NAME = "news"

SAME_NEWS_SIMILARITY_THRESHOLD = 0.9

cloudAMQP_client = CloudAMQPClient(DEDUPE_NEWS_TASK_QUEUE_URL, DEDUPE_NEWS_TASK_QUEUE_NAME)


def handle_message(msg):
    if msg is None or not isinstance(msg,dict):
        return

    task = msg
    text = task['text']
    if text is None:
        return

    published_at = parser.parse(task['publishedAt'])
    published_at_day_begin = datetime.datetime(published_at.year, published_at.month, published_at.day,0,0,0,0)
    published_at_day_end = published_at_day_begin + datetime.timedelta(days=1)

    db = mongodb_client.get_db()
    same_day_news_list = list(db[NEWS_TABLE_NAME].find({
        'publishedAt':{
            '$gte': published_at_day_begin,
            '$lt': published_at_day_end
        }
    }))

    if same_day_news_list is not None and len(same_day_news_list) > 0:
        documents = [x['text'] for x in same_day_news_list]
        documents.insert(0, text)

        tfidf =TfidfVectorizer().fit_transform(documents)
        sim_mat = tfidf * tfidf.T
        print sim_mat

        rows, _ = sim_mat.shape

        for row in range(1, rows):
            similarity = sim_mat[row,0]
            if similarity > SAME_NEWS_SIMILARITY_THRESHOLD:
                print 'Ignore duplicates'
                return

    task['publishedAt'] = parser.parse(task['publishedAt'])

    title = task['title']
    if title is not None:
        topic = news_topic_modeling_service_client.classify(title)
        task['class'] = topic
    db[NEWS_TABLE_NAME].replace_one({'digest': task['digest']}, task, upsert=True)

    LOGGING_NEWS_DEDUPER.info("inserted:1")

while True:
    if cloudAMQP_client is not None:
        msg = cloudAMQP_client.getMessage()
        try:
            handle_message(msg)
        except Exception as e:
            print "news_deduper: " + e
            pass

        cloudAMQP_client.sleep(SLEEP_TIME_IN_SECONDS)


