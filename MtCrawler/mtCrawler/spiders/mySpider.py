# -*- coding: utf-8 -*-
# filename: mySpider.py
# 用于定义爬虫程序的一些公共的接口
import sys
reload(sys)
sys.setdefaultencoding('utf-8') 

class MySpider(object):
    def __init__(self):
        pass
    #用于对网页内容进行过滤接口
    def filter(self,content):
        return content
    #返回实际网站名接口
    def getWebName(self):
        return "其它"
    #返回实际版块名接口
    def getSectionName(self):
        return "其它版块"