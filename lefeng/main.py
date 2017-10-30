__author__ = 'bobby'

from scrapy.cmdline import execute

import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
#execute(["scrapy", "crawl", "lefeng"])
# execute(["scrapy", "crawl", "meili"])
execute(["scrapy", "crawl", "quchenshi"])