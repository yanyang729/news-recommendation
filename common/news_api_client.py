import requests
import json

NEWS_API_ENDPOINT = 'https://newsapi.org/v1/'
ARTICLES_API = 'articles'

BBC_NEWS = 'bbc-news'
BBC_SPORT = 'bbc-sport'
CNN = 'cnn'

DEFAULT_SOURCES = [CNN, BBC_NEWS]
SORT_BY_TOP = 'top'
NEWS_API_KEY = '5df1f9be52c84f82bde43875f141303f'


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