# -*- coding: utf-8 -*-
# Command: scrapy genspider -t csvfeed csvfeed_spider quotes.toscrape.com
# Create spider with csvfeed template
from scrapy.spiders import CSVFeedSpider


class CsvfeedSpiderSpider(CSVFeedSpider):
    name = 'csvfeed_spider'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/feed.csv']
    # headers = ['id', 'name', 'description', 'image_link']
    # delimiter = '\t'

    # Do any adaptations you need here
    #def adapt_response(self, response):
    #    return response

    def parse_row(self, response, row):
        i = {}
        #i['url'] = row['url']
        #i['name'] = row['name']
        #i['description'] = row['description']
        return i
