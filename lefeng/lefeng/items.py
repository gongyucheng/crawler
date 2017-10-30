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

    def get_insert_sql(self):

        insert_sql = """
                 insert ignore into product_copy(productName, img,brand, remark, description,number,guige,place,category)' \
        #              'VALUES (%s, %s, %s, %s,%s,%s,%s,%s,%s)
              """
        # ON DUPLICATE KEY UPDATE content=VALUES(fav_nums)

        params = (
             self["productName"], self["img"], self["brand"], self["remark"] or "", self["description"] or "",
             self["number"], self["guige"] or "", self["place"] or "", self["category"])
        return insert_sql, params

    pass
#美丽修行item
class MeiLiItem(scrapy.Item):
    img = scrapy.Field()
    productName = scrapy.Field()
    englishName = scrapy.Field()
    nickname = scrapy.Field()  #昵称
    importRecord =scrapy.Field()#进口备案
    ingredient = scrapy.Field()

    def get_insert_sql(self):
        insert_sql = """
               insert ignore into meiliProduct(img,productName,englishName,nickname,importRecord,ingredient)
               VALUES (%s, %s, %s, %s, %s,%s)
           """

        params = (self["img"], self["productName"], self["englishName"], self["nickname"],
                   self["importRecord"],self["ingredient"])
        return insert_sql, params

class MeiLiIngredientItem(scrapy.Item):
    name = scrapy.Field()
    englishName = scrapy.Field()
    nickname = scrapy.Field()
    casNumber= scrapy.Field()  # 昵称
    purpose = scrapy.Field()  # 进口备案
    brief = scrapy.Field() #简介
    def get_insert_sql(self):
        insert_sql = """
               insert into meiliIngredient(name,englishName,nickname,casNumber,purpose,brief)
               VALUES (%s, %s, %s, %s, %s,%s)
           """
        # ON DUPLICATE KEY UPDATE content=VALUES(fav_nums)

        params = (self["name"], self["englishName"], self["nickname"], self["casNumber"],
                   self["purpose"], self["brief"])
        return insert_sql, params