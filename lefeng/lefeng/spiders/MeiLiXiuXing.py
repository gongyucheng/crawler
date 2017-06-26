import re
import scrapy
import datetime
from scrapy.http import Request
from urllib import parse
from scrapy.loader import ItemLoader
from lefeng.items import LefengItem
import time

class LeFengListSprider(scrapy.Spider):

    # global page
    # page = 1

    name = "meilixiuxing"

    allowed_domains = ["search.lefeng.com","product.lefeng.com","a2.vimage1.com","list.lefeng.com"]
    url = 'http://search.lefeng.com/search/showresult?keyword=%%E9%%9D%%A2%%E8%%86%%9C&is_has_stock=0&page=%d&moreBrand=0' % (1)
    start_urls = [url]

    def parse(self, response):
        """
        1. 获取文章列表页中的文章url并交给scrapy下载后并进行解析
        2. 获取下一页的url并交给scrapy进行下载， 下载完成后交给parse
        """

        #解析列表页中的所有文章url并交给scrapy下载后并进行解析
        post_nodes = response.css("#productDivGroup .pruwrap  a")
        for post_node in post_nodes:
            image_url = post_node.css("img::attr(src)").extract_first("")
            post_url = post_node.css("::attr(href)").extract_first("")
            yield Request(url=parse.urljoin(response.url, post_url), meta={"front_image_url":image_url}, callback=self.parse_detail)

        #提取下一页并交给scrapy进行下载
       # next_url = response.css(".next.page-numbers::attr(href)").extract_first("")
        global page
        page += 1
        #next_url = 'http://search.lefeng.com/search/showresult?keyword=%%E9%%9D%%A2%%E8%%86%%9C&is_has_stock=0&page=%d&moreBrand=0' % (page)
        #next_url = 'http://search.lefeng.com/search/showresult?keyword=%%E9%%98%%B2%%E6%%99%%92%%E9%%9A%%94%%E7%%A6%%BB&is_has_stock=0&page=%d&moreBrand=0' % (page)  # 防晒套装
        #next_url = 'http://search.lefeng.com/search/showresult?keyword=%%E6%%B4%%81%%E9%%9D%%A2&is_has_stock=0&page=%d&moreBrand=0' % ( page)  # 洁面分类
        #next_url = 'http://search.lefeng.com/search/showresult?keyword=%%E9%%9D%%A2%%E9%%83%%A8%%E6%%8A%%A4%%E8%%82%%A4&is_has_stock=0&page=%d&moreBrand=0' % (page)  # 面部护肤分类
        #next_url = 'http://search.lefeng.com/search/showresult?keyword=%%E7%%9C%%BC%%E9%%83%%A8%%E6%%8A%%A4%%E7%%90%%86&is_has_stock=0&page=%d&moreBrand=0' % (page)  # 眼部护理分类
        #next_url = 'http://search.lefeng.com/search/showresult?keyword=%%E7%%9C%%BC%%E5%%A6%%86&is_has_stock=0&page=%d&moreBrand=0' % (page)  # 眼妆
        #next_url = 'http://search.lefeng.com/search/showresult?keyword=%%E5%%94%%87%%E5%%A6%%86&is_has_stock=0&page=%d&moreBrand=0' % (page)  # 唇妆
        #next_url = 'http://search.lefeng.com/search/showresult?keyword=%%E5%%8D%%B8%%E5%%A6%%86&is_has_stock=0&page=%d&moreBrand=0' % (page)  # 卸妆
        #next_url = 'http://search.lefeng.com/search/showresult?keyword=%%E7%%BE%%8E%%E7%%94%%B2&is_has_stock=0&page=%d&moreBrand=0' % (page)  # 美甲
        # next_url = 'http://search.lefeng.com/search/showresult?keyword=%%E7%%BE%%8E%%E5%%AE%%B9%%E5%%B7%%A5%%E5%%85%%B7&is_has_stock=0&page=%d&moreBrand=0' % (page)  # 美容工具
        #
        # #过滤掉非数字
        # def isNumber(x):
        #     try:
        #        return int(x)
        #     except:
        #         return  False
        #
        #
        #
        # pages = response.css(".com_page .pages a::text").extract()
        #
        # page_list = list(filter(isNumber, pages))
        # print(page_list)
        # max_page = max(page_list)
        # if next_url and page<max_page:
        #     yield Request(url=parse.urljoin(response.url, next_url), callback=self.parse)

    def parse_detail(self, response):
       # article_item = LefengItem()
        article_item = self.setDefaultContent()
        img = response.meta.get("front_image_url", "")  #文章封面图

       # category_title = response.meta.get("category_title","")


        article_item["img"] = img

        tab = response.css(".detail-info-table tr")
        for td in tab:
            list = td.css("td::text").extract()

            if list[0] == "商品名称:":
                print(list[1])
                article_item["productName"] = list[1]
            elif list[0] == "商品品牌:":
                article_item["brand"] = list[1]
            elif list[0] == "备注:":
                article_item["remark"] = list[1]
            elif list[0] == "规格:":
                article_item["guige"] = list[1]
            elif list[0] == "特点描述:":
                article_item["description"] = list[1]
            elif list[0] == "产地:":
                article_item["place"] = list[1]
            elif list[0] == "货号:":
                article_item["number"] = list[1]

        #print(article_item)
        return article_item

    def setDefaultContent(self):
            article_item = LefengItem()
            article_item["productName"] = ""

            article_item["brand"] = ""
            article_item["remark"] = ""
            article_item["guige"] = ""

            article_item["description"] = ""

            article_item["place"] = ""

            article_item["number"] = ""
            return article_item

