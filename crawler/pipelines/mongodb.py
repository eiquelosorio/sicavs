import pymongo

from config.AppConfig import AppConfig


class MongoDBPipeline(object):

    def __init__(self, mongo_uri, mongo_db, mongo_collection):
        self.db = None
        self.client = None
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
        self.mongo_collection = mongo_collection

    @classmethod
    def from_crawler(cls, crawler):
        crawler_config = AppConfig()
        return cls(
            mongo_uri=crawler_config.mongo_uri,
            mongo_db=crawler_config.mongo_db,
            mongo_collection=crawler_config.mongo_collection_sicavs_temp
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db[self.mongo_collection].insert_one(dict(item))
        return item
