# encoding: utf-8
import pymongo
from scrapy.core.downloader.handlers import http
from scrapy.utils.project import get_project_settings


class IPProxyMiddleware(object):

    def fetch_proxy(self):
        # You need to rewrite this function if you want to add proxy pool
        # the function should return a ip in the format of "ip:port" like "12.34.1.4:9090"
        return None


