from services import ScrapCollectionsService
from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess
from scrapy.utils.log import configure_logging
from spiders.SicavsSpider import SicavsSpider


class SicavsScrapService:

    def __init__(self, collections_service: ScrapCollectionsService):
        self.collections_service = collections_service

    def start_crawler(self):
        self.collections_service.clean_temp_sicavs_collection()

        configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s'})
        process = CrawlerProcess(settings=get_project_settings())
        process.crawl(SicavsSpider)
        process.start()

        self.collections_service.merge_sicavs_updates()
        self.collections_service.close_connections()
