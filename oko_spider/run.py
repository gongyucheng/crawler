__author__ = 'gary'

from scrapy.crawler import CrawlerProcess
from scrapy.cmdline import execute
import sys
import os
from scrapy.utils.project import get_project_settings
from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from oko_spider.spiders.MeiLiXiuXing import MeiLiXiuXing
from oko_spider.spiders.LeFengListSprider import LeFengListSprider
from oko_spider.spiders.Quchenshi import QuchenshiSpider

from scrapy.utils.log import configure_logging
# sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# execute(["scrapy", "crawl", "meili"])

if __name__ == '__main__':
    argu1 = sys.argv[1]

    configure_logging()
    a = get_project_settings()
    runner = CrawlerRunner(a)
    if argu1 == "meili":
        d = runner.crawl(MeiLiXiuXing)
    elif argu1 == "lefeng":
        d = runner.crawl(LeFengListSprider)
    elif argu1 == "watsons":
        d = runner.crawl(QuchenshiSpider)
    else:
        d = runner.crawl(MeiLiXiuXing)
        d = runner.crawl(QuchenshiSpider)
        d = runner.crawl(LeFengListSprider)
    d.addBoth(lambda _: reactor.stop())

    reactor.run() # the script wi
    #
    #print(sys.argv[0])
    for i in range(0, len(sys.argv)):
        print(sys.argv[i])