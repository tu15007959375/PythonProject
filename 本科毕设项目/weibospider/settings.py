# -*- coding: utf-8 -*-

BOT_NAME = 'spider'

SPIDER_MODULES = ['spiders']
NEWSPIDER_MODULE = 'spiders'

ROBOTSTXT_OBEY = False

# change cookie to yours
DEFAULT_REQUEST_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:61.0) Gecko/20100101 Firefox/61.0',
    'Cookie': '_T_WM=3de9d06a9579e6584a1b944bb3bc0e69; '
              'SCF=AvKe_9qsmlB1kWq61pLZ8XlMB5oll4-4gV2nrAE3rpnO1FQSQ1P2FLPOFNrvTshe5hs3OjorKs2uut2j2m1x-Yg.; '
              'SUB=_2A25PpSc_DeRhGeNH41MX8yvEyTuIHXVtZkl3rDV6PUJbktANLRLmkW1NSnsHmYqJRLsxMO3z97Zgyw2qdMTVRUs9; '
              'SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9Wh1RiOZDmvL6slZg3vFVIs75NHD95Qf1KnpSoef1hzNWs4Dqcjci--Xi-zRi-2Ri'
              '--Ni-24i-iWi--NiK.4i-i2i--Xi-zRi-zci--ci-27i-ihi--Xi-zRi-2R; SSOLoginState=1654740847'}
CONCURRENT_REQUESTS = 16

DOWNLOAD_DELAY = 2

DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.cookies.CookiesMiddleware': None,
    'scrapy.downloadermiddlewares.redirect.RedirectMiddleware': None,
    'middlewares.IPProxyMiddleware': 100,
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 101,
}

ITEM_PIPELINES = {
    'pipelines.MongoDBPipeline': 300,
}

MONGO_HOST = '127.0.0.1'
MONGO_PORT = 27017
