import os
from dotenv import load_dotenv


class AppConfig:
    def __init__(self):
        load_dotenv()
        print('sisisis')
        self.mongo_uri = 'mongodb://db:27017'
        self.mongo_db = 'sicavs'
        self.mongo_collection_mirror_sicavs = 'mirror_sicavs'
        self.mongo_collection_sicavs_changes = 'sicavs_changes'
        self.mongo_collection_sicavs_temp = 'sicavs_temp'
