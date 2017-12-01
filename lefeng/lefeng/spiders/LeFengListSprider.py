#!/usr/bin/python
# Filename: func_global.py
import re
import scrapy
import datetime
from scrapy.http import Request
from urllib import parse
from scrapy.loader import ItemLoader
from lefeng.items import LefengItem

import time

class LeFengListSprider(scrapy.Spider):

    name = "lefeng"

    allowed_domains = ["search.lefeng.com","product.lefeng.com","a2.vimage1.com","list.lefeng.com"]
    #resid_key = 'myspider:lefeng_url'
    url = "http://list.lefeng.com"
    start_urls = [url]


    def parse(self, response):
        """
        1. 获取文章列表页中的文章url并交给scrapy下载后并进行解析
        2. 获取下一页的url并交给scrapy进行下载， 下载完成后交给parse
        """
        # 获取所有分类link，并迭代加载分类列表首页
        post_nodes = response.css(".aKindsBox .akList .akli a")
        for post_node in post_nodes:
            #image_url = post_node.css("img::attr(src)").extract_first("")
            post_url = post_node.css("::attr(href)").extract_first("")
            category_title = post_node.css("::text").extract_first("")
            page = 1

            yield Request(url=post_url,
                          callback=lambda  response,category = category_title,page = page:self.parse_homepage(response,category,page))

#解析分类列表首页数据，获取缩略图，获取下一页
    def parse_homepage(self,response,category,page):
        post_nodes = response.css("#productDivGroup .pruwrap  a")
        #print(post_nodes)
        for post_node in post_nodes:
            image_url = post_node.css("img::attr(src)").extract_first("")
            post_url = post_node.css("::attr(href)").extract_first("")
            yield Request(url=parse.urljoin(response.url, post_url), meta={"front_image_url":image_url,"category_title":category}, callback=self.parse_detail)

        # global  page
        # page = 1

        # next_url = 'http://search.lefeng.com/search/showresult?keyword=%%E7%%BE%%8E%%E5%%AE%%B9%%E5%%B7%%A5%%E5%%85%%B7&is_has_stock=0&page=%d&moreBrand=0' % (
        #     page)  # 美容工具
        # next_url = response.url + '&is_has_stock=0&page=%d&moreBrand=0' % (page)

        # 过滤掉非数字
        def isNumber(x):
            try:
                return int(x)
            except:
                return False

        pages = response.css(".com_page .pages a::text").extract()

        page_list = list(filter(isNumber, pages))
        print(page_list)
        #获取最大页数
        max_page = int(page_list[-1])
     #迭代分类所有页面数据
        while max_page>1:
            max_page = max_page-1
            next_url = response.url + '&is_has_stock=0&page=%d&moreBrand=0' % (max_page)
            yield Request(url=parse.urljoin(response.url, next_url),
                          callback=lambda response, category=category: self.parse_list(response, category))

 #迭代循环分类列表页面
    def parse_list(self,response,category):
        post_nodes = response.css("#productDivGroup .pruwrap  a")
        # print(post_nodes)
        for post_node in post_nodes:
            image_url = post_node.css("img::attr(src)").extract_first("")
            post_url = post_node.css("::attr(href)").extract_first("")
            yield Request(url=parse.urljoin(response.url, post_url),
                          meta={"front_image_url": image_url, "category_title": category}, callback=self.parse_detail)
#解析详情页
    def parse_detail(self, response):
       # article_item = LefengItem()
        article_item = self.setDefaultContent()
        img = response.meta.get("front_image_url", "")  #文章封面图

        category_title = response.meta.get("category_title","")


        article_item["img"] = img
        article_item["category"] = category_title
        article_item["url"] = response.url
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




