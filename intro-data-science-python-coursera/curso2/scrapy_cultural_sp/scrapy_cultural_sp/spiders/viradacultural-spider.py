from scrapy.selector import Selector
from scrapy.http import Request
from scrapy_cultural_sp.items import Atracao
from scrapy.contrib.spiders import CrawlSpider
from datetime import date
from datetime import datetime
import unicodedata

class ViradaCulturalSpider(CrawlSpider):
    name = "virada_cultural"
    start_urls = ["http://www.viradaculturalpaulista.sp.gov.br"]

    def parse(self, response):
        body_sel = Selector(response)
        urls_cidade = body_sel.xpath("//div[@class='item']//p//a//@href").extract()

        for url in urls_cidade:
            yield Request(url, self.parse_atracao())

    def parse_atracao(self, response):
        body_sel = Selector(response)
        cidade = self.to_str(body_sel.xpath("//h1/text()"))
        endereco = self.to_str(body_sel.xpath("//span[@class='address']/text()"))
        atracao = self.to_str(body_sel.xpath("//h4[@class='title']//a/text()"))

    def to_str(self, selector):
        return selector.extract()[0].encode("utf-8")
