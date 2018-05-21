# -*- coding: utf-8 -*-
# Command: scrapy genspider -t xmlfeed basic_spider docs.wprssaggregator.com
# Create spider with xmlfeed template
from scrapy.spiders import XMLFeedSpider
from try_scrapy.items import TryScrapyItem


class XmlfeedSpiderSpider(XMLFeedSpider):
    name = "xmlfeed_spider"
    allowed_domains = ["docs.wprssaggregator.com"]
    start_urls = ["https://docs.wprssaggregator.com/feed/"]
    iterator = "iternodes"  # you can change this; see the docs
    itertag = "item"  # change it accordingly

    def parse_node(self, response, node):
        self.logger.info(
            "Hi, this is a <%s> node!: %s", self.itertag, "".join(node.extract())
        )

        item = TryScrapyItem()
        item["link"] = node.xpath("link").extract()
        item["name"] = node.xpath("title").extract_first()
        item["description"] = node.xpath("description").extract()
        return item
