# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from oko_spider import config

#美丽修行item
class MeiLiItem(scrapy.Item):

    url = scrapy.Field()
    img = scrapy.Field()
    productName = scrapy.Field()
    englishName = scrapy.Field()
    nickname = scrapy.Field()  #昵称
    importRecord =scrapy.Field()#进口备案
    ingredient = scrapy.Field()

    def get_insert_sql(self):
        insert_sql = """
               insert ignore into %s""" % config.MEILI_PRODUCT_TABLE_NAME + """(img,productName,englishName,nickname,importRecord,ingredient)
               VALUES (%s, %s, %s, %s, %s,%s)
           """

        params = (self["img"], self["productName"], self["englishName"], self["nickname"],
                   self["importRecord"],self["ingredient"])
        return insert_sql, params
#成分item
class MeiLiIngredientItem(scrapy.Item):

    url = scrapy.Field()
    name = scrapy.Field()
    englishName = scrapy.Field()
    nickname = scrapy.Field()
    casNumber= scrapy.Field()
    purpose = scrapy.Field()
    brief = scrapy.Field() #简介
    def get_insert_sql(self):
        insert_sql = """
               insert into %s""" % config.MEILI_INGREDIENT_TABLE_NAME + """(name,englishName,nickname,casNumber,purpose,brief)
               VALUES (%s, %s, %s, %s, %s,%s)
           """
        # ON DUPLICATE KEY UPDATE content=VALUES(fav_nums)

        params = (self["name"], self["englishName"], self["nickname"], self["casNumber"],
                   self["purpose"], self["brief"])
        return insert_sql, params



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
                        insert ignore into %s""" % config.LEFENG_PRODUCT_TABLE_NAME +"""(productName, img,brand, remark, description,number,guige,place,category)
                            VALUES (%s, %s, %s, %s,%s,%s,%s,%s,%s)
                     """
        # ON DUPLICATE KEY UPDATE content=VALUES(fav_nums)

        params = (
             self["productName"], self["img"], self["brand"], self["remark"] or "", self["description"] or "",
             self["number"], self["guige"] or "", self["place"] or "", self["category"])
        return insert_sql, params

    pass
class WatsonsItem(scrapy.Item):

    url = scrapy.Field()
    brand = scrapy.Field()        # 品牌
    productName = scrapy.Field()  # 商品名
    productSeriesName = scrapy.Field()  # 商品系列名称
    images = scrapy.Field()       # 图片, 多张, 大图, 逗号分隔
    spec = scrapy.Field()       #  规格
    description = scrapy.Field() # 产品信息, HTML 文本
    place = scrapy.Field()      # 产地
    category = scrapy.Field()   # 分类, :分隔的多个词语, 如 皮肤护理:面部护理:面膜
    price = scrapy.Field()      # 价格

    def get_insert_sql(self):
        insert_sql = """
        insert into %s""" % config.WATSONS_PRODUCT_TABLE_NAME + """(brand, productName, productSeriesName, images, spec, description, place, category, price)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        params = (self["brand"], self["productName"], self["productSeriesName"], self["images"],
                       self["spec"], self["description"],self["place"],self["category"],self["price"])
        return insert_sql, params
