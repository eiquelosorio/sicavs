import pymongo

from config.AppConfig import AppConfig


class ScrapCollectionsService:

    def __init__(self, app_config: AppConfig):
        self.mirror_collection_name = app_config.mongo_collection_mirror_sicavs
        self.changes_collection_name = app_config.mongo_collection_sicavs_changes
        self.temp_collection_name = app_config.mongo_collection_sicavs_temp
        self.client = pymongo.MongoClient(app_config.mongo_uri)
        self.db = self.client[app_config.mongo_db]

    def clean_temp_sicavs_collection(self):
        self.db.drop_collection(self.temp_collection_name)

    def merge_sicavs_updates(self):
        temp_collection = self.db[self.temp_collection_name]
        mirror_collection = self.db[self.mirror_collection_name]
        changes_collection = self.db[self.changes_collection_name]

        for sicav in temp_collection.find():
            isin = sicav['isin']
            current_sicav = mirror_collection.find_one({'isin': isin})

            new_sicav_history = self.__sicav_copy(sicav)
            update_doc = {'isin': isin, 'changes': [new_sicav_history]}

            if current_sicav:
                if self.__has_sicavs_changed(current_sicav, sicav):
                    changes_collection.update_one({'isin': isin}, {'$addToSet': {'changes': new_sicav_history}})
            else:
                changes_collection.insert_one(update_doc)

            mirror_collection.update_one({'isin': isin}, {'$set': new_sicav_history}, upsert=True)

    def close_connections(self):
        self.client.close()

    def __has_sicavs_changed(self, current, scraped) -> bool:
        updated_fields = ['dom', 'capInic', 'capMax', 'dateLast']

        for field in updated_fields:
            if current[field] != scraped[field]:
                return True
        return False

    def __sicav_copy(self, sicav):
        copy = sicav.copy()
        copy.pop('isin')
        copy.pop('_id')
        return copy
