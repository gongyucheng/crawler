__author__ = 'gary'

from scrapy.crawler import CrawlerProcess
from scrapy.cmdline import execute
import sys
import os
from scrapy.utils.project import get_project_settings

# sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# execute(["scrapy", "crawl", "meili"])

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
    process.crawl('meili', domain='scrapinghub.com')
    process.start()  # the script will block here until the crawling is finished