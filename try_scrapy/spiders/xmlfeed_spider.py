# -*- coding: utf-8 -*-
from scrapy.spiders import XMLFeedSpider
from try_scrapy.items import TryScrapyItem


class XmlfeedSpiderSpider(XMLFeedSpider):
    name = "xmlfeed_spider"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["http://quotes.toscrape.com/feed.xml"]
    iterator = "iternodes"  # you can change this; see the docs
    itertag = "item"  # change it accordingly

    def parse_node(self, response, node):
        self.logger.info('Hi, this is a <%s> node!: %s', self.itertag, ''.join(node.extract()))

        item = TryScrapyItem()
        item['id'] = node.xpath('@id').extract()
        item['name'] = node.xpath('name').extract()
        item['description'] = node.xpath('description').extract()
        return item

