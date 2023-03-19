import os
from dotenv import load_dotenv


class AppConfig:
    def __init__(self):
        load_dotenv()

        self.mongo_uri = os.getenv('MONGO_URI')
        self.mongo_db = os.getenv('MONGO_DB')
        self.mongo_collection_mirror_sicavs = os.getenv('MONGO_COLLECTION_MIRROR_SICAVS')
        self.mongo_collection_sicavs_changes = os.getenv('MONGO_COLLECTION_SICAVS_CHANGES')
        self.mongo_collection_sicavs_temp = os.getenv('MONGO_COLLECTION_SICAVS_TEMP')
