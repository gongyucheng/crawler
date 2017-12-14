__author__ = 'gary'

from scrapy.crawler import CrawlerProcess
from scrapy.cmdline import execute
import sys
import os
from scrapy.utils.project import get_project_settings
from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from meilixiuxing.spiders.MeiLiXiuXing import MeiLiXiuXing
from scrapy.utils.log import configure_logging
import meilixiuxing.settings as setting
# sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# execute(["scrapy", "crawl", "meili"])

if __name__ == '__main__':
    # configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s'})
    # #settings = get_project_settings()
    a = get_project_settings()
    print(get_project_settings())
    runner = CrawlerRunner(a)
    d = runner.crawl(MeiLiXiuXing)

    d.addBoth(lambda _: reactor.stop())
    configure_logging()
    reactor.run() # the script wi
    # process = CrawlerProcess(get_project_settings())
    #
    # # 'followall' is the name of one of the spiders of the project.
    # #process.crawl('meili', domain='scrapinghub.com')
    # process.crawl('meili')
    # process.start()  # the script will block here until the crawling is finished