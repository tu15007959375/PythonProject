# -*- coding: utf-8 -*-

from pymongo.errors import DuplicateKeyError

from items import RelationshipItem, TweetItem
from pymongo import MongoClient
from items import UserItem


class MongoDBPipeline(object):
    def __init__(self):
        client = MongoClient(host='127.0.0.1', port=27017)
        db = client.get_database("weibo")
        self.Users = db["Users"]
        self.Tweets = db.get_collection("Tweet")

        self.Relationships = db["Relationships"]

    def process_item(self, item, spider):
        if spider.name == 'UserSpider':
            if isinstance(item, RelationshipItem):
                self.insert_item(self.Relationships, item)
            elif isinstance(item, UserItem):
                self.insert_item(self.Users, item)
            elif isinstance(item, TweetItem):
                self.insert_item(self.Tweets, item)
        return item

    @staticmethod
    def insert_item(collection, item):
        try:
            collection.insert_one(dict(item))
        except DuplicateKeyError:
            pass
