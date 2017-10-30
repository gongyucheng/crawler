# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QuchenshiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
# class QuchenshiItem(scrapy.Item):
#     brandName = scrapy.Field()#品牌名
#     name = scrapy.Field()  # 商品名
#     categoryName = scrapy.Field()#品类
#     colorType = scrapy.Field()#颜色分类
#     specification = scrapy.Field() #规格
#     brief = scrapy.Field() #简介
#     # def get_insert_sql(self):
#     #     insert_sql = """
#     #            insert into meiliIngredient(name,englishName,nickname,casNumber,purpose,brief)
#     #            VALUES (%s, %s, %s, %s, %s,%s)
#     #        """
#     #     # ON DUPLICATE KEY UPDATE content=VALUES(fav_nums)
#     #
#     #     params = (self["name"], self["englishName"], self["nickname"], self["casNumber"],
#     #                self["purpose"], self["brief"])
#     #     return insert_sql, params

class WatsonsItem(scrapy.Item):
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
        insert into watsons_copy1(brand, productName, productSeriesName, images, spec, description, place, category, price)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        params = (self["brand"], self["productName"], self["productSeriesName"], self["images"],
                       self["spec"], self["description"],self["place"],self["category"],self["price"])
        return insert_sql, params