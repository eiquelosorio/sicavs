import unittest
import pymongo
from config.AppConfig import AppConfig
from services.ScrapCollectionsService import ScrapCollectionsService
from services.SicavsRepository import SicavsRepository
from services.SicavsScrapService import SicavsScrapService


class SicavsScrapperTest(unittest.TestCase):

    def setUp(self):
        self.app_config = AppConfig()
        self.client = pymongo.MongoClient(self.app_config.mongo_uri)
        self.db = self.client[self.app_config.mongo_db]
        self.db.drop_collection(self.app_config.mongo_collection_sicavs_temp)
        self.collection = self.db[self.app_config.mongo_collection_sicavs_temp]
        self.sicavs_repo = SicavsRepository(app_config=self.app_config)

    def test_data_extraction(self):
        scrap_service = SicavsScrapService(
            collections_service=ScrapCollectionsService(
                app_config=self.app_config
            )
        )
        scrap_service.start_crawler()
        item_count = self.collection.count_documents({})
        self.assertGreater(item_count, 0)

    def test_get_sicavs(self):
        sicavs = self.sicavs_repo.get_sicavs(isin='ES0109642035')
        self.assertEqual(len(sicavs), 1)
        item = sicavs[0]
        self.assertEqual(item.get('noReg'), '1480')
        self.assertEqual(item.get('name'), '1948 INVERSIONS, SICAV S.A.')

    def test_get_sicav_data(self):
        sicav = self.sicavs_repo.get_sicav_data(isin='ES0109642035')
        self.assertIsNotNone(sicav)
        changes = sicav.get('changes')
        self.assertIsNotNone(changes)
        self.assertGreater(len(changes), 0)
        first_change = changes[0]
        self.assertEqual(first_change.get('noReg'), '1480')
        self.assertEqual(first_change.get('name'), '1948 INVERSIONS, SICAV S.A.')


    def tearDown(self):
        self.db.drop_collection(self.app_config.mongo_collection_sicavs_temp)
        self.client.close()
