import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    # start_urls = ["http://quotes.toscrape.com/page/1/"]

    def start_requests(self):
        url = "http://quotes.toscrape.com/"
        tag = getattr(self, "tag", None)
        if tag:
            url = "{0}tag/{1}".format(url, tag)
        yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        for quote in response.css("div.quote"):
            yield {
                "text": quote.css("span.text::text").extract_first(),
                "author": quote.css("small.author::text").extract_first(),
                # "tags": quote.css("div.tag a.tag::text").extract(),
            }
        # for href in response.css("li.next a::attr(href)"):
        #     yield response.follow(href, callback=self.parse)
        for a in response.css("li.next a"):
            yield response.follow(a, callback=self.parse)
