# -*- coding: utf-8 -*-
# Command: scrapy genspider -t basic basic_spider quotes.toscrape.com
# Create spider with basic template
import scrapy


class BasicSpiderSpider(scrapy.Spider):
    name = "basic_spider"
    allowed_domains = ["quotes.toscrape.com"]
    # start_urls = ["http://quotes.toscrape.com/"]

    def start_requests(self):
        url = "http://quotes.toscrape.com/login"
        response = scrapy.Request(url)
        csrf_token = response.xpath(
            "//input[(@name='csrf_token')]/@value"
        )  # AttributeError: 'Request' object has no attribute 'xpath'
        return [
            scrapy.FormRequest(
                url,
                formdata={
                    "username": "boba", "password": "test", "csrf_token": csrf_token
                },
                callback=self.logged_in,
            )
        ]

    def logged_in(self, response):
        is_login = response.xpath("//a[@href='/logout']")
        if is_login:
            print("You logged in!")
        else:
            print("Login error!!!")

    def parse(self, response):
        pass
