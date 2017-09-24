# coding:utf-8
'''
Logging module for Tap News
'''

import os
import logging
import logging.config as log_conf

print __file__

LOG_DIR = os.path.dirname(__file__)+'/logs'
if not os.path.exists(LOG_DIR):
    os.mkdir(LOG_DIR)

LOG_PATH = os.path.join(LOG_DIR, 'news.log')

LOG_CONFIG = {
    'version': 1.0,
    'formatters': {
        'simple': {
            'format': '%(name)s %(levelname)s %(message)s',
        },
        'detail': {
            'format': '%(name)s %(levelname)s %(message)s',
            # 'datefmt': "%Y-%m-%d %H:%M:%S"
        },
        'optional': {
            'format': '%(filename)s %(lineno)d %(levelname)s %(message)s',
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'INFO',
            'formatter': 'optional'
        },
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 10,
            'filename': LOG_PATH,
            'level': 'INFO',
            'formatter': 'detail',
            'encoding': 'utf-8',
        },
    },
    'loggers': {
        'news_deduper': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
        },
        'other': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
        }

    }
}

log_conf.dictConfig(LOG_CONFIG)


LOGGING_NEWS_DEDUPER = logging.getLogger('news_deduper')
LOGGING_OHTER = logging.getLogger('other')

__all__ = [ 'LOGGING_NEWS_DEDUPER', 'LOGGING_OHTER']