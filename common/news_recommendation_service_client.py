import pyjsonrpc
import json

with open("../config/common_config.json") as f:
    config = json.load(f)['news_recommendation_service_client']

URL = config['URL']

client = pyjsonrpc.HttpClient(url=URL)

def getPreferenceForUser(userId):
    preference = client.call('getPreferenceForUser', userId)
    print "Preference list: %s" % str(preference)
    return preference
