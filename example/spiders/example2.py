# -*- coding: utf-8 -*-
import scrapy
from example.items import ExampleItem
from scrapy import Request
from urllib.parse import urljoin
from urllib.parse import urlparse


# noinspection PyMissingOrEmptyDocstring
class Example2Spider(scrapy.Spider):
    name = 'example2'
    start_urls = ['https://www.tripadvisor.com.tr/Restaurants-g297977-Bursa.html']

    def parse(self, response):

        for href in response.xpath("//div[@class='title']/a[@class='property_title']/@href"):
            url = response.urljoin(href.extract())
            yield Request(url, callback=self.parse_page)

        next_page = response.xpath("//div[contains(@class, 'unified')]/a[contains(@class, 'next')]/@href")
        if next_page:
            url = response.urljoin(next_page[0].extract())
            yield Request(url, self.parse)

    def parse_page(self, response):
        item = ExampleItem()
        titleRestaurant = response.xpath("//div[contains(@class, 'restaurantName')]/h1/text()").extract()
        address = response.xpath("//span[contains(@class, 'detailLinkText--co3ei')]/text()").extract()
        state = response.xpath("//span[@class='extended-adress')]/text()").extract()
        city = response.xpath("//span[@class='locality')]/text()").extract()
        country = response.xpath("//span[@class='country-name')]/text()").extract()
        mobile = response.xpath("//span[contains(@class, 'mobile')]/text()").extract()
        kitchenType = response.xpath("//div[@class='header_links')]/a/text()").extract()
        rating = response.xpath("//span[contains(@class, 'detailLinkText--co3ei')]/text()").extract()[0]
        reviewTitles = response.xpath("//span[@class='noQuotes')]/text()").extract()
        reviewTitle = reviewTitles[0].encode("utf8")
        contents = response.xpath("//div[@class, 'entry']/p/text()").extract()
        content = contents[0].encode("utf-8")

        item['titleRestaurant'] = titleRestaurant()
        item['address'] = address()
        item['state'] = state()
        item['city'] = city()
        item['country'] = country()
        item['mobile'] = mobile()
        item['kitchenType'] = kitchenType()
        item['rating'] = rating()
        item['reviewTitle'] = reviewTitle()
        item['content'] = content()

        yield item



