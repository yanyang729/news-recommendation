import requests
import random
import os
from lxml import html

USER_AGENTS_FILE =
USER_AGENTS = []

with open(USER_AGENTS_FILE, 'r') as f:
    for ua in f.readlines():
        if ua:
            USER_AGENTS.append(ua.strip()[1:-1])

def getHeader():
    ua = random.choice(USER_AGENTS)
    headers = {
        "Connection": "close",
        "User-Agent": ua
    }
    return headers


def extract_news(news_url):
    session_requests = requests.session()
    response = session_requests.get(news_url, headers=getHeader())
    news = {}

    try:
        tree = html.fromstring(response.content)
        response