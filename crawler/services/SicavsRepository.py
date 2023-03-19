import pymongo

from config.AppConfig import AppConfig


class SicavsRepository:

    def __init__(self, app_config: AppConfig):
        self.mirror_collection_name = app_config.mongo_collection_mirror_sicavs
        self.changes_collection_name = app_config.mongo_collection_sicavs_changes
        self.client = pymongo.MongoClient(app_config.mongo_uri)
        self.db = self.client[app_config.mongo_db]

    def get_sicavs(self, isin=None, creation_date=None, register_number=None, name=None):
        collection = self.db[self.mirror_collection_name]
        filter = {}

        if creation_date:
            filter['dateOffReg'] = creation_date
        if register_number:
            filter['noReg'] = register_number
        if name:
            filter['name'] = name
        if isin:
            filter['isin'] = isin

        return list(collection.find(filter))

    def get_sicav_data(self, isin):
        collection = self.db[self.changes_collection_name]
        return collection.find_one({
            'isin': isin
        })
