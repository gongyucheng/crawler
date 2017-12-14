# -*- coding: utf-8 -*-
import random, base64
from scrapy.exceptions import IgnoreRequest
from oko_spider import config

class MeiLiXiuXingProxyMiddleware(object):
    proxyList = [ \
        '111.1.23.215:80', '183.131.76.27:8888', '110.251.132.22:808', '110.77.169.30:8080', '58.246.194.70:8080',
        '159.232.214.68:8080'
    ]
    def process_request(self, request, spider):
        # Set the location of the proxy
        redis_key = ""
        if spider.name == "meili":
            redis_key = config.REDIS_MEILI_URL_KEY
        elif spider.name == "lefeng":
            redis_key = config.REDIS_LEFENG_URL_KEY
        elif spider.name == "quchenshi":
            redis_key = config.REDIS_WATSONS_URL_KEY
        if config.redis_db.hexists(redis_key, request.url):
            raise IgnoreRequest("Duplicate item found: %s" % request.url)
        # pro_adr = random.choice(self.proxyList)
        # print("USE PROXY -> " + pro_adr)
        # request.meta['proxy'] = "http://" + pro_adr
        else:
            return None