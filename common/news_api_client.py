import requests
import json

NEWS_API_ENDPOINT = 'https://newsapi.prg/v1/'
# TODO: add api key
NEWS_API_KEY = ''

ARTICLES_API = 'articles'

BBC_NEWS = 'bbc-news'
BBC_SPORT = 'bbc-sport'
CNN = 'cnn'

DEFAULT_SOURCES = [CNN, BBC_NEWS]
SORT_BY_TOP = 'top'


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

        response = requests.get(buildUrl(), params=payload)

        res_json = json.loads(response.content)

        if res_json and res_json['status'] == 'ok' and res_json['source']:
            for news in res_json['articles']:
                news['source'] = res_json['source']

            articles += news['source']
    return articles