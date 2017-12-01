from twisted.internet import reactor
import scrapy
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from lefeng.spiders import  LeFengListSprider
from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess
from os.path import dirname
import os
import sys

#需要引用外层文件夹中文件，将工程中的所有文件夹加入环境变量中
path = dirname(os.path.abspath(os.path.dirname(__file__)))
sys.path.append(path)

if __name__ == '__main__':
    # configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s'})
    # #settings = get_project_settings()
    # runner = CrawlerRunner()
    #
    # d = runner.crawl(LeFengListSprider)
    #
    # d.addBoth(lambda _: reactor.stop())
    #
    # reactor.run() # the script wi
    process = CrawlerProcess(get_project_settings())

    # 'followall' is the name of one of the spiders of the project.
    process.crawl('lefeng', domain='scrapinghub.com')
    process.start()  # the script will block here until the crawling is finished