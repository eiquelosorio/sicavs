import scrapy
from items.SICAVSItem import SICAVSItem


class SicavsSpider(scrapy.Spider):
    name = 'sicavs-spider'
    start_urls = ['https://www.cnmv.es/Portal/Consultas/MostrarListados.aspx?id=18']

    custom_settings = {
        'ITEM_PIPELINES': {
            'pipelines.MongoDBPipeline': 1
        }
    }

    def parse(self, response):
        npage = response.xpath(
            "//span[@id='ctl00_ContentPrincipal_wucRelacionRegistros_MF_wucPaginadorRepeaterAnterior_lblInfoPaginacion']//text()").get()
        npage = int(npage.split()[-1])

        yield from self.parsepage(response)
        # for i in range(1, npage):
        #     yield scrapy.Request(response.url + f"&page={i}", callback=self.parsepage)

    def parsepage(self, response):
        links = response.xpath("//ul[@id='listaElementosPrimernivel']//a//@href").extract()
        for link in links:
            url = response.urljoin(link)
            yield scrapy.Request(url, callback=self.parseNIF)

    def parseNIF(self, response):
        item = SICAVSItem()
        item["name"] = response.xpath("//span[@id='ctl00_ContentPrincipal_lblSubtitulo']//text()").get()

        tds = response.xpath("//table[@id='ctl00_ContentPrincipal_gridDatos']//tr//td")
        item["noReg"] = tds[0].xpath(".//text()").get()
        item["dateOffReg"] = tds[1].xpath(".//text()").get()
        item["dom"] = tds[2].xpath(".//text()").get()
        item["capInic"] = tds[3].xpath(".//text()").get()
        item["capMax"] = tds[4].xpath(".//text()").get()
        item["isin"] = tds[5].xpath(".//a//text()").get()
        item["dateLast"] = tds[6].xpath(".//text()").get()

        yield item
