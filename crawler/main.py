from config.AppConfig import AppConfig
from services.ScrapCollectionsService import ScrapCollectionsService
from services.SicavsScrapService import SicavsScrapService

if __name__ == '__main__':
    scrap_service = SicavsScrapService(
        collections_service=ScrapCollectionsService(
            app_config=AppConfig()
        )
    )
    scrap_service.start_crawler()
