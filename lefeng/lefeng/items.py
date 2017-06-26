# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LefengItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    img = scrapy.Field()
    brand = scrapy.Field()
    productName = scrapy.Field()
    remark = scrapy.Field()
    guige = scrapy.Field()
    description = scrapy.Field()
    place = scrapy.Field()
    number = scrapy.Field()
    category = scrapy.Field()

    pass
