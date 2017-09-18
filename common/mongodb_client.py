from pymongo import MongoClient
import os
import sys
import json

with open(os.path.join(os.path.dirname(__file__),'..','config','common_config.json')) as f:
    config = json.load(f)

config_mongodb_client = config['mongodb_client']

client = MongoClient('%s:%s' % (config_mongodb_client['MONGO_DB_HOST'], config_mongodb_client['MONGO_DB_PORT']))

def get_db(db=config_mongodb_client['DB_NAME']):
    return client[db]
