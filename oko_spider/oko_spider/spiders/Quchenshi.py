import re
import scrapy
import datetime
from scrapy.http import Request
from  oko_spider.items import WatsonsItem
from urllib import parse
import redis,time,threading
from scrapy.loader import ItemLoader
import time
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
class QuchenshiSpider(scrapy.Spider):
    name = 'quchenshi'


    allowed_domains = ['watsons.com.cn']
    start_urls = [
        'http://www.watsons.com.cn/c/Skincare',
        'http://www.watsons.com.cn/c/Haircare',
        'http://www.watsons.com.cn/c/PersonalCare',
        'http://www.watsons.com.cn/c/Men',
        'http://www.watsons.com.cn/c/Cosmetics',

    ]
    # def start_request:
    #     #login
    url = 'http://www.watsons.com.cn'
    def parse(self, response):
        list = response.css(".proListBox .proListImg a")
        #print(list.extract_first(""))
        for node in list:
            image_url =node.css("img::attr(src)").extract_first("")
            post_url = node.css("::attr(href)").extract_first("")
            yield Request(url=parse.urljoin(response.url, post_url),
                          meta={"ua": True}, callback=self.parseProduct)
            #print(post_url)


        nextlink = response.xpath('//div[@class="turnPage fr mr57"]/a[@class="next"]/@href').extract()
        if nextlink:
            link = nextlink[0]
            print('next==',self.url+link)
            yield Request(self.url + link, callback=self.parse)
        #print("next",nextlink)
    # def parse_detail(self, response):
    #     img = response.meta.get("front_image_url", "")  # 文章封面图
    #     print(img)

    def parseProduct(self, response):
        def splitStr(x):
            a = x.split(":")
            #print(a)
            #print("///////////",a[1])
            #print(re.sub('[\r\n\t<b></b> <p></p>]','',a[0]))
            if len(a) > 1:
                return {re.sub('[\r\n\t<b></b> <p></p>]','',a[0]):a[1]}
            else:
                return {"":""}
            #return x.split(":")
        """
        从商品详情页中获取信息, 返回 Item
        """
        item = self.setDefaultItem()
        item['url'] = response.url
        item['brand'] = response.css('p.skuBrand::text').extract_first("").strip()
        item['productSeriesName'] = response.css('h5::text').extract_first("").strip()
        item['productName'] = response.css('h3.skuName::text').extract_first("").strip()
        item['price'] = response.css('p.skuPrice i::text').extract_first("").strip()
        item['images'] = ','.join(response.xpath("//div[@class='slide']/img/@supersrc").extract())
        a =  response.css('div.skuSelect p em::text')
        spec = response.css('div.skuSelect p em::text').extract()
        item['spec'] = ""
        if len(spec) > 0:
            item['spec'] = spec[-1].strip()
        #item['spec'] = response.css('div.skuSelect p em::text')[-1].extract().strip()
        item['description'] = response.css('div.skuInfo.skuInfoHeight p').extract_first("")
        #item['place'] = ""
        item['category'] = ""
        b = response.css('div.skuInfo p').extract_first("")
        list1 = list(map(splitStr,b.split('<br>')))
        for placeDict in list1:
            if  "产地" in placeDict.keys():
                item['place'] = placeDict["产地"]
        print(list1)
        return  item
    def setDefaultItem(self):
        item = WatsonsItem()
        item['url'] = ""
        item['brand'] = ""
        item['productSeriesName'] = ""
        item['productName'] = ""
        item['price'] = ""
        item['images'] = ""
        item['spec'] = ""

        item['spec'] = ""
        # item['spec'] = response.css('div.skuSelect p em::text')[-1].extract().strip()
        item['description'] = ""
        # item['place'] = ""
        item['category'] = ""
        item['place'] = ""
        return  item