__author__ = 'gary'

import sys
sys.path.append('./lefeng')
sys.path.append('./meilixiuxing')
import os
from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from lefeng.lefeng.spiders.LeFengListSprider import LeFengListSprider
from meilixiuxing.spiders.MeiLiXiuXing import MeiLiXiuXing
from scrapy.utils.log import configure_logging
#导入获取项目配置的模块
from scrapy.utils.project import get_project_settings
import meilixiuxing.settings
if __name__ == '__main__':
#   os.system("python runLefeng.py")
#configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s'})
  # configure_logging()
  # runner = CrawlerRunner(meilixiuxing.settings)
  # #runner.crawl(LeFengListSprider)
  # runner.crawl(MeiLiXiuXing)
  # d = runner.join()
  # d.addBoth(lambda _: reactor.stop())
  # reactor.run()  # the script will block here until the crawl