import random, base64
from scrapy.exceptions import IgnoreRequest
from quchenshi import config


class ProxyMiddleware(object):
    proxyList = [ \
        '111.1.23.215:80', '183.131.76.27:8888', '110.251.132.22:808','110.77.169.30:8080','58.246.194.70:8080','159.232.214.68:8080'
    ]

    def process_request(self, request, spider):
        # Set the location of the proxy
        if config.redis_db.hexists(config.REDIS_MEILI_URL_KEY, request.url):
            raise IgnoreRequest("Duplicate item found: %s" % request.url)
        # pro_adr = random.choice(self.proxyList)
        # print("USE PROXY -> " + pro_adr)
        # request.meta['proxy'] = "http://" + pro_adr
        else:
            return None