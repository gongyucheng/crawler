# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import MySQLdb
import MySQLdb.cursors
from twisted.enterprise import adbapi
from scrapy.exceptions import  DropItem
from quchenshi import config

class QuchenshiPipeline(object):
    def process_item(self, item, spider):
        return item
class MysqlTwistedPipline(object):
    def __init__(self, dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls, settings):
        dbparms = dict(
            host=config.MYSQL_HOST,
            db=config.MYSQL_DBNAME,
            user=config.MYSQL_USER,
            passwd=config.MYSQL_PASSWORD,
            charset='utf8',
            port=config.MYSQL_PORT,
            cursorclass=MySQLdb.cursors.DictCursor,
            use_unicode=True,
        )
        dbpool = adbapi.ConnectionPool("MySQLdb", **dbparms)

        return cls(dbpool)

    def process_item(self, item, spider):
        #使用twisted将mysql插入变成异步执行
        query = self.dbpool.runInteraction(self.do_insert, item)
        query.addErrback(self.handle_error, item, spider) #处理异常
        # 如果redis里存在这个url，就抛出一个错误的item
        if config.redis_db.hexists(config.REDIS_MEILI_URL_KEY, item['url']):
            raise DropItem("Duplicate item found: %s" % item)
        else:
            # 存储url进入redis里
            config.redis_db.hset(config.REDIS_MEILI_URL_KEY, item['url'],0)

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