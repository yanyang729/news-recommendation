import pyjsonrpc
import json
import os
import sys

with open(os.path.join(os.path.dirname(__file__),'..','config','common_config.json')) as f:
    config = json.load(f)['news_topic_modeling_service_client']

URL = config['URL']

client = pyjsonrpc.HttpClient(url=URL)


def classify(text):
    topic = client.call('classify', text)
    print 'Topic: %s' % topic
    return topic