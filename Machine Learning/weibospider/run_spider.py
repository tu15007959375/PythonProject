#!/usr/bin/env python
# encoding: utf-8

import os

from scrapy.crawler import CrawlerProcess

from scrapy.utils.project import get_project_settings
from spiders.Users import Users

if __name__ == '__main__':
    mode_to_spider = {
        'UserSpider': Users,
    }
    count = 1
    os.environ['SCRAPY_SETTINGS_MODULE'] = f'settings'
    settings = get_project_settings()
    process = CrawlerProcess(settings)
    process.crawl(mode_to_spider['UserSpider'])
    process.start()
