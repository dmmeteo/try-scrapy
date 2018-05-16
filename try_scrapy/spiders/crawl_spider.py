# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class CrawlSpiderSpider(CrawlSpider):
    name = "crawl_spider"
    allowed_domains = ["bigl.ua"]
    start_urls = ["https://bigl.ua/all_categories"]

    rules = (
        # Extract links matching 'Noutbuki' and 'Monitory' (but not matching 'Kompyutery')
        # and follow links from them (since no callback means follow=True by default).
        Rule(LinkExtractor(allow=("Monitory",), deny=("Kompyutery",))),
        # Extract links matching 'monitor' and 'lenovo' and parse them with the spider's method parse_item
        Rule(LinkExtractor(allow=("Noutbuki",)), callback="parse_item"),
    )

    def parse_item(self, response):
        # TODO normal parser
        self.logger.info("Hi, this is an item page! %s", response.url)
        item = scrapy.Item()
        item["url"] = response.url
        item["title"] = response.xpath(
            '//h1[@data-qaid="title-h1"]/text()'
        ).extract_first().strip()
        item["price"] = response.xpath(
            '//span[@data-qaid="product-price"]/text()'
        ).extract_first().strip()
        return item
