# -*- coding: utf-8 -*-
# filename: dnyct_spider.py
# 用于抓取猎云网 东南亚创投部分内容
import scrapy
import urlparse
import handle
import time
from scrapy.http import Request
from mySpider import MySpider

class dnyctSpider(scrapy.Spider,MySpider):
    name = "dnyct_spider"
    allowed_domains = ["lieyunwang.com"]
    start_urls = [
        "http://www.lieyunwang.com/dongnanya",
    ]

    def __init__(self):
        #网页文章中需要删除的字段
        self.__filterKey = "你的项目也想被报道"
        #爬取的网站名
        self.__webName = "猎云网"
        #爬取的版块名
        self.__sectionName = "东南亚创投"
        self.__successCount = 0
    
    #从起始网页开始抓取
    def parse(self, response):
        #开始日志
        print "----Crawler Run[" + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) + "]:" + self.__webName + " " + self.__sectionName + " startUrl:" +  self.start_urls[0]

        self.__successCount = 0
        url_records = response.xpath('//*[@id="article-container-box"]/div[3]/div[2]/div[1]/ul//li/div/a/@href').extract()
        totalCount = len(url_records)
        for url_record in url_records:
            url = urlparse.urljoin(response.url, url_record)
            yield Request(url=url, callback=self.parse_news)
        #结束日志
        print "----Crawler End[" + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) + "]:" + self.__webName + " " + self.__sectionName + " Count:" +  str(totalCount) + " insertCount:" + str(self.__successCount) + " errCount:" + str(totalCount - self.__successCount)
        print ""
        
    
    def parse_news(self, response):
        title = ''.join(response.xpath('//*[@id="bbbox"]/div[2]/div[2]/div/h1/text()').extract())
        content = ''.join(response.xpath('//*[@id="bbbox"]/div[2]/div[2]/div/div[2]//p/text()').extract())
        url = response.url
        #实际处理
        if handle.handle(self,title,content,url,self.__webName) == 0:
            #如果处理成功
            self.__successCount += 1

    def filter(self,content):
        # 将这个字段以及后面的内容全部截取掉
        nPos = content.decode('utf-8').index(self.__filterKey.decode('utf-8'))
        if nPos > 0:
            content = content[0:nPos]
        return content
    
    def getWebName(self):
        return self.__webName
    
    def getSectionName(self):
        return self.__sectionName