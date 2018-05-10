import scrapy


class BiglSpider(scrapy.Spider):
    name = "bigl"

    start_urls = ["https://bigl.ua/Noutbuki"]

    def parse(self, response):
        # follow links to product page
        for href in response.css("a.bgl-product__title::attr(href)"):
            yield response.follow(href, callback=self.parse_product)

        # follow pagination links
        for href in response.css("a.bgl-pager__item:last-child::attr(href)"):
            yield response.follow(href, callback=self.parse)

    def parse_product(self, response):

        def extract_with_css(query):
            return response.css(query).extract_first().strip()

        yield {
            "url": response.url.split("?")[0],
            "title": extract_with_css("h1.ui-text::text"),
        }
