import os
import sys

from newspaper import Article

sys.path.append(os.path.join(os.path.dirname(__file__),'..','common'))

from cloudAMQP_client import CloundAMQPClient as CloudAMQPClient

DEDUPE_NEWS_TASK_QUEUE_URL = "amqp://rcsdmawz:QDrDPYaGXyAA0WU8NiVWopTTH3yVkULw@wasp.rmq.cloudamqp.com/rcsdmawz"
DEDUPE_NEWS_TASK_QUEUE_NAME = "news-deduper"
SCRAPE_NEWS_TASK_QUEUE_URL = "amqp://holajbod:izGGmsaUFTKfY1gOSSeTN8N466Yi6_1C@crane.rmq.cloudamqp.com/holajbod"
SCRAPE_NEWS_TASK_QUEUE_NAME = "news-task"


SLEEP_TIME_IN_SECONDS = 5

dedupe_news_queue_client = CloudAMQPClient(DEDUPE_NEWS_TASK_QUEUE_URL, DEDUPE_NEWS_TASK_QUEUE_NAME)
scrape_news_queue_client = CloudAMQPClient(SCRAPE_NEWS_TASK_QUEUE_URL, SCRAPE_NEWS_TASK_QUEUE_NAME)


def handle_message(msg):
    """
    from NEWS API response, use newspaper pkg download article and then it to deduper MQ
    """
    if msg is None or not isinstance(msg,dict):
        print 'message is broken'
        return

    task = msg

    article = Article(task['url'])
    article.download()
    article.parse()

    task['text'] = article.text.encode('utf-8')

    dedupe_news_queue_client.sendMessage(task)


while True:
    if scrape_news_queue_client is not None:
        msg = scrape_news_queue_client.getMessage()
        try:
            handle_message(msg)
        except Exception as e:
            print e
            pass

    scrape_news_queue_client.sleep(SLEEP_TIME_IN_SECONDS)

