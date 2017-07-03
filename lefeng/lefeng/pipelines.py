# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import codecs
import json
import MySQLdb
import MySQLdb.cursors
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exporters import JsonItemExporter
from twisted.enterprise import adbapi
from scrapy.http import Request

class LefengPipeline(object):
    def process_item(self, item, spider):
        return item

class JsonExporterPipleline(object):
    #调用scrapy提供的json export导出json文件
    def __init__(self):
        self.file = open('articleexport.json', 'wb')
        self.exporter = JsonItemExporter(self.file, encoding="utf-8", ensure_ascii=False)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

# class ArticleImagePipeline(ImagesPipeline):
#     def get_media_requests(self, item, info):
#         # for image_url in item['img']:
#         #     yield Request(image_url)
#             yield Request(item['img'])
#     def item_completed(self, results, item, info):
#         if "front_image_url" in item:
#             for ok, value in results:
#                 image_file_path = value["path"]
#             item["front_image_path"] = image_file_path
#
#         return item

class MysqlPipeline(object):
    #采用同步的机制写入mysql
    def __init__(self):
        self.conn = MySQLdb.connect(host='localhost',user='root', passwd='123456', db='mianmo', port=3306,charset="utf8",use_unicode=True)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):

        insert_sql = 'insert ignore into demo(productName, img,brand, remark, description,number,guige,place)' \
                     'VALUES (%s, %s, %s, %s,%s,%s,%s,%s)'
        self.cursor.execute(insert_sql, (
        item["productName"], item["img"], item["brand"], item["remark"] or "", item["description"] or "",
        item["number"], item["guige"] or "", item["place"] or ""))

        self.conn.commit()

class MysqlTwistedPipline(object):
    def __init__(self, dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls, settings):
        dbparms = dict(
            host = settings["MYSQL_HOST"],
            db = settings["MYSQL_DBNAME"],
            user = settings["MYSQL_USER"],
            passwd = settings["MYSQL_PASSWORD"],
            charset='utf8',
            port = 3306,
            cursorclass=MySQLdb.cursors.DictCursor,
            use_unicode=True,
        )
        dbpool = adbapi.ConnectionPool("MySQLdb", **dbparms)

        return cls(dbpool)

    def process_item(self, item, spider):
        #使用twisted将mysql插入变成异步执行
        query = self.dbpool.runInteraction(self.do_insert, item)
        query.addErrback(self.handle_error, item, spider) #处理异常

    def handle_error(self, failure, item, spider):
        # 处理异步插入的异常
        print (failure)

    def do_insert(self, cursor, item):
        #执行具体的插入
        #根据不同的item 构建不同的sql语句并插入到mysql中
        insert_sql, params = item.get_insert_sql()
        cursor.execute(insert_sql, params)
        # insert_sql = 'insert ignore into product(productName, img,brand, remark, description,number,guige,place,category)' \
        #              'VALUES (%s, %s, %s, %s,%s,%s,%s,%s,%s)'
        # cursor.execute(insert_sql, (
        #     item["productName"], item["img"], item["brand"], item["remark"] or "", item["description"] or "",
        #     item["number"], item["guige"] or "", item["place"] or "", item["category"]))
