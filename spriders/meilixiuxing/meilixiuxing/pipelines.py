# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import codecs
import json
import MySQLdb
import MySQLdb.cursors
from scrapy.exceptions import  DropItem
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exporters import JsonItemExporter
from twisted.enterprise import adbapi
#from scrapy import log
from scrapy.http import Request
from meilixiuxing import config

#redis_db = redis.Redis(host='127.0.0.1',port=6379)
#redis_data_dict = 'f_url'
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

class MysqlTwistedPipline(object):
    def __init__(self, dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls, settings):
        dbparms = dict(
            host = config.MYSQL_HOST,
            db=config.MYSQL_DBNAME,
            user=config.MYSQL_USER,
            passwd=config.MYSQL_PASSWORD,
            charset='utf8',
            port=config.MYSQL_PORT,
            cursorclass=MySQLdb.cursors.DictCursor,
            use_unicode=True,
        )
        dbpool = adbapi.ConnectionPool("MySQLdb", **dbparms)
        #redis_db = redis.Redis(host=settings['REDIS_HOST'],port=settings['REDIS_PORT'],db=settings['REDIS_DB'])
        return cls(dbpool)

    def process_item(self, item, spider):
        #使用twisted将mysql插入变成异步执行
        query = self.dbpool.runInteraction(self.do_insert, item)
        query.addErrback(self.handle_error, item, spider) #处理异常
        #redis_db.hset(redis_data_dict,item['url'])
        #如果redis里存在这个url，就抛出一个错误的item
        if config.redis_db.hexists(config.REDIS_MEILI_URL_KEY,item['url']):
            raise DropItem("Duplicate item found: %s" % item)
        else:
            #存储url进入redis里
            config.redis_db.hset(config.REDIS_MEILI_URL_KEY,item['url'],0)
        return item

    def handle_error(self, failure, item, spider):
        # 处理异步插入的异常
        log.msg(failure, level=log.DEBUG)
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
