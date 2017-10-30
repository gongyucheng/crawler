import re
import scrapy
import datetime
from scrapy.http import Request
from urllib import parse
from scrapy.loader import ItemLoader
from lefeng.items import MeiLiItem
from lefeng.items import MeiLiIngredientItem
import time
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from  selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

class Quchenshi(scrapy.Spider):

    name = "quchenshi"
    allowed_domains = ["watsons.com.cn"]
    url = 'http://www.watsons.com.cn/c/Skincare'
    start_urls = [url]
    # rules = (
    #     # 提取匹配 'category.php' (但不匹配 'subsection.php') 的链接并跟进链接(没有callback意味着follow默认为True)
    #     Rule(LinkExtractor(allow=(r'.*/product\?category=\d+',)),callback='parse_home',follow=True),
    #
    #     # 提取匹配 'item.php' 的链接并使用spider的parse_item方法进行分析
    #     #Rule(LinkExtractor(allow=(r'.*/product/.*\.html',)), callback='parse_detail'),
    # )
    #
    # def __init__(self):
    #     CrawlSpider.__init__(self)
    #     # use any browser you wish
    #     self.browser = webdriver.PhantomJS('/Users/gary/Downloads/phantomjs-2.1.1-macosx/bin/phantomjs')
    #
    # def __del__(self):
    #     self.browser.close()
    def parse(self, response):
        category_id_list = response.css(".goods-category li")
        for i in category_id_list:
            categoryid = i.css("::attr(data-id)").extract_first("")
            list_url = "https://www.bevol.cn/product?category=%s" % (categoryid)
            yield Request(url=list_url, meta={'PhantomJS': True,"category_id":categoryid},
                          callback=self.parse_home)

    # def start_requests(self):
    #     return [Request("https://www.bevol.cn/product?category=6", meta={'PhantomJS': True}, callback=self.parse)]
    #     # request.meta['PhantomJS'] = True
    #     # return request
    def parse_home(self,response):
        # 过滤掉非数字
        def isNumber(x):
            try:
                return int(x)
            except:
                return False


        pages = response.css(".foot-page .tcdPageCode a::text").extract()

        page_list = list(filter(isNumber, pages))
        print(page_list)
        # 获取最大页数
        max_page = int(page_list[-1])
        list_page = 0
        categoryid = response.meta["category_id"]
        while list_page<max_page:
            list_page += 1
            link = "product?v=2.0&category=%s&p=%d" % (categoryid,list_page)
            print(parse.urljoin(response.url, link))
            yield Request(url=parse.urljoin(response.url, link),meta={'PhantomJS': True},
                          callback=self.parse_list)



            # moredata = self.isMoreData(parse.urljoin(response.url, link))
            # if moredata == False:
            #     break

    def parse_list(self,response):

        pages = response.css(".page-content a")
        for i in pages:
            #img = i.xpath("//img/text()").extract()
            img = i.css("img::attr(src)").extract_first("")
            if img != "https://img0.bevol.cn/Goods/default.png@90p":
                link = i.css("::attr(href)").extract_first("")
                detail_url = parse.urljoin(response.url, link)
                url1 = "http://list.lefeng.com"
                yield Request(url=parse.urljoin(response.url, link),meta={"ua":True},
                             callback=self.parse_detail,errback=self.error_detail)
                # yield Request(url=url1,
                #               callback="parse_detail")

    def error_detail(self,response):
        print(response)
    def parse_detail(self,response):

        productName = response.css(".cosmetics-info-title .cosmetics-info-title-text .p1::text").extract_first("")
        ingredient_link = response.css(".cosmetics-info-left .chengfenbiao .table a::attr(href)").extract()
        for link in ingredient_link:
            yield Request(url=parse.urljoin(response.url, link), meta={"productName": productName, "ua": True},
                          callback=self.parse_Ingredient, errback=self.error_ingredient)


        product  = self.setDefaultProduct()

        product["img"] = response.css(".cosmetics-info-title-img img::attr(src)").extract_first("")
        product["productName"] = response.css(".cosmetics-info-title .cosmetics-info-title-text .p1::text").extract_first("")
        product["englishName"] = response.css(
            ".cosmetics-info-title .cosmetics-info-title-text .p2::text").extract_first("")
        product["nickname"] = response.css(
            ".cosmetics-info-title .cosmetics-info-title-text .p3::text").extract_first("")
        product["importRecord"] = response.css(
            ".cosmetics-info-title .cosmetics-info-title-text .p5::text").extract_first("")

        ingredient_links = response.css(".cosmetics-info-left .chengfenbiao .table a")
        ingredientName = self.getIngredientName(ingredient_links)

        product["ingredient"] = ingredientName


        #print(article_item)
        yield product

    def error_ingredient(self,response):
        print(response)
    def parse_Ingredient(self,response):
        p = response.css(".component-info-title p::text").extract()
        ingredient_item = self.setDefaultIngredient()
        ingredient_item["name"] = response.css(".component-info-title h1::text").extract_first("")
        ingredient_item["englishName"] = p[0]
        ingredient_item["nickname"] = p[1]
        ingredient_item["casNumber"] = p[2]
        ingredient_item["purpose"] =  p[3]
        ingredient_item["brief"] = response.css(".cosmetics-info-title .component-info-box p::text").extract_first("")

        yield ingredient_item

    # def isMoreData(self,url):
    #     self.browser.get(url)
    #     # self.browser.get("https://www.bevol.cn/product?v=2.0&category=6&p=8")
    #     page_source = self.browser.page_source
    #
    #     # 使用scrapy selecor解析网络返回的数据
    #     t_selector = Selector(text=page_source)
    #     # pages = t_selector.css(".page-content a::attr(href)").extract()
    #     p = t_selector.css(".page-content .search-more p::text").extract()
    #     if p == "对不起，没有搜索到您要的结果，美丽修行建议您：":
    #         return False
    #     else:
    #         return True

    def setDefaultProduct(self):
            article_item = MeiLiItem()
            article_item["productName"] = ""
            article_item["img"] = ""
            article_item["englishName"] = ""
            article_item["nickname"] = ""
            article_item["importRecord"] = ""

            return article_item

    def setDefaultIngredient(self):
            article_item = MeiLiIngredientItem()
            article_item["name"] = ""
            article_item["nickname"] = ""
            article_item["casNumber"] = ""
            article_item["purpose"] = ""
            article_item["brief"] = ""
            article_item["englishName"] = ""

            return article_item
    def getIngredientName(self,list):
        ingredientName = ""
        for a in list:
            ingredient = a.css("::text").extract_first("")
            ingredientName = ingredientName + ingredient +","

        return ingredientName