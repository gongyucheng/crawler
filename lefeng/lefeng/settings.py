# -*- coding: utf-8 -*-
import os
# Scrapy settings for lefeng project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'lefeng'

SPIDER_MODULES = ['lefeng.spiders']
NEWSPIDER_MODULE = 'lefeng.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'lefeng (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'lefeng.middlewares.LefengSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'lefeng.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   #'lefeng.pipelines.LefengPipeline': 300,
#'scrapy.pipelines.images.ImagesPipeline': 3,
 #'lefeng.pipelines.JsonExporterPipleline': 3,
 #'lefeng.pipelines.ArticleImagePipeline': 3,
   # 'lefeng.pipelines.MysqlPipeline':2,
  'lefeng.pipelines.MysqlTwistedPipline': 3,
}
IMAGES_URLS_FIELD = "front_image_url"
project_dir = os.path.abspath(os.path.dirname(__file__))
IMAGES_STORE = os.path.join(project_dir, 'images/防晒')

# 爬取间隔
#DOWNLOAD_DELAY = 0.25

# 禁用cookie
COOKIES_ENABLED = False

SPIDER_MIDDLEWARES = {
   'scrapy_deltafetch.DeltaFetch': 50,
   #'scrapy_magicfields.MagicFieldsMiddleware': 51,
}
DELTAFETCH_ENABLED = True
# MAGICFIELDS_ENABLED = True
# MAGIC_FIELDS = {
#     #"timestamp": "$time",
#     "spider": "$spider:name",
#     "url": "scraped from $response:url",
#     "domain": "$response:url,r'https?://([\w\.]+)/']",
# }

# # 重写默认请求头
# DEFAULT_REQUEST_HEADERS = {
#     'Accept': 'text/html, application/xhtml+xml, application/xml',
#     'Accept-Language': 'zh-CN,zh;q=0.8',
#     'Host': 'ip84.com',
#     'Referer': 'http://ip84.com/',
#     'X-XHR-Referer': 'http://ip84.com/'
# }

# 激活自定义UserAgent和代理IP
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#     'lefeng.useragent.UserAgent': 1,
#     'lefeng.proxymiddlewares.ProxyMiddleware': 100,
#     'scrapy.downloadermiddleware.useragent.UserAgentMiddleware': None,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


MYSQL_HOST = "localhost"
MYSQL_DBNAME = "mianmo"
MYSQL_USER = "root"
MYSQL_PASSWORD = "123456"
