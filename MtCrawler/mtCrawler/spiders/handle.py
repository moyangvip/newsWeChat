# -*- coding: utf-8 -*-
# filename: handle.py
# 用于实际处理抓取到的数据
import web

#加入BosonNLP的摘要处理库
import sys
sys.path.append("../BosonNLP/")
from summary import Summary

summaryObj = Summary()
#连接数据库
db = web.database(dbn='mysql', db='WeChatDB', user='root', pw='123456')

def handle(spider,title,content,url,webName):
    #过滤内容
    content = spider.filter(content)

    url = url.strip()
    title = title.strip()
    content = content.strip()
    #获得摘要
    summary = summaryObj.getSummary("",content).strip()
    return insertDB(url,title,summary,spider.getWebName(),spider.getSectionName())

def insertDB(url_,title_,summary_,webName_,sectionName_):
    newsInfoList  = []
    #首先尝试查询该标题是否已经存在
    strWhere = "newsTitle = \'" + title_ + "\'"
    newsInfos = db.select("NewsInfo", where=strWhere )
    #将查询到的数据存入list
    for newsInfo in newsInfos:
        newsInfoList.append(newsInfo)
    if len(newsInfoList) != 0:
        #该标题已经存在，不再插入
        return 1
    try:
        db.insert('NewsInfo', newsUrl=url_,newsSummary=summary_,newsTitle=title_,webName=webName_,sectionName=sectionName_)
    except Exception,ex:
        #如果插入发生异常
        return 1
    return 0
