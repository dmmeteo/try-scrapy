# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import SitemapSpider


class SitemapSpiderSpider(SitemapSpider):
    name = "sitemap_spider"
    sitemap_urls = ["http://smscoin.com/robots.txt"]
    # sitemap_urls = ['http://smscoin.com/sitemap.txt']
    sitemap_rules = [
        ("/shop/", "parse_shop"),
        ("/product/", "parse_product"),
        ("/category/", "parse_category"),
    ]

    other_urls = ["http://smscoin.com/about"]

    def start_requests(self):
        requests = list(super(SitemapSpiderSpider, self).start_requests())
        requests += [scrapy.Request(x, self.parse_other) for x in self.other_urls]
        return requests

    def parse_shop(self, response):
        pass  # ... scrape shop here ...

    def parse_other(self, response):
        pass  # ... scrape other here ...

    def parse_product(self, response):
        pass  # ... scrape product ...

    def parse_category(self, response):
        pass  # ... scrape category ...
