from datetime import datetime

from scrapy import Item, Field


class SICAVSItem(Item):
    name = Field()
    noReg = Field()
    dateOffReg = Field()
    dom = Field()
    capInic = Field()
    capMax = Field()
    isin = Field()
    dateLast = Field()
    scrapedAt = Field()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self['scrapedAt'] = datetime.now()


