import requests
import json

with open("../config/common_config.json") as f:
    config = json.load(f)['news_api_client']

NEWS_API_ENDPOINT = config['NEWS_API_ENDPOINT']
ARTICLES_API = config['ARTICLES_API']

BBC_NEWS = config['BBC_NEWS']
BBC_SPORT = config['BBC_SPORT']
CNN = config['CNN']

DEFAULT_SOURCES = [CNN, BBC_NEWS]
SORT_BY_TOP = config['SORT_BY_TOP']
NEWS_API_KEY = config['NEWS_API_KEY']


def buildUrl(endPoint=NEWS_API_ENDPOINT, apiName=ARTICLES_API):
    return endPoint + apiName


def getNewsFromSource(sources=DEFAULT_SOURCES, sortBy=SORT_BY_TOP):
    articles = []

    for source in sources:
        payload = {
            'apiKey': NEWS_API_KEY,
            'source': source,
            'sortBy': sortBy
        }

        response = requests.get(buildUrl(), params=payload,verify=False)

        res_json = json.loads(response.content)

        if res_json and res_json['status'] == 'ok' and res_json['source']:
            for article in res_json['articles']:
                article['source'] = res_json['source']
            articles += res_json['articles']

    return articles