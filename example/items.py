# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class ExampleItem(scrapy.Item):

    titleRestaurant = scrapy.Field()
    address = scrapy.Field()
    state = scrapy.Field()
    city = scrapy.Field()
    country = scrapy.Field()
    mobile = scrapy.Field()
    kitchenType = scrapy.Field()
    rating = scrapy.Field()
    reviewTitle = scrapy.Field()
    content = scrapy.Field()

