# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

#乐蜂item
class LefengItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    img = scrapy.Field()
    brand = scrapy.Field()
    productName = scrapy.Field()
    remark = scrapy.Field()
    guige = scrapy.Field()
    description = scrapy.Field()
    place = scrapy.Field()
    number = scrapy.Field()
    category = scrapy.Field()

    def get_insert_sql(self):

        insert_sql = """
                 insert ignore into lefeng(productName, img,brand, remark, description,number,guige,place,category)
                     VALUES (%s, %s, %s, %s,%s,%s,%s,%s,%s)
              """
        # ON DUPLICATE KEY UPDATE content=VALUES(fav_nums)

        params = (
             self["productName"], self["img"], self["brand"], self["remark"] or "", self["description"] or "",
             self["number"], self["guige"] or "", self["place"] or "", self["category"])
        return insert_sql, params

    pass