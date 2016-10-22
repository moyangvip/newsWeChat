# -*- coding: utf-8 -*-
# filename: msgManger.py
# 用于处理待返回的消息内容

import random
from usrInfo import UsrInfo
#随机权值匹配，根据权值返回任意一条消息，权值越高，返回该消息的几率越大
class DefaultManager(object):
    def __init__(self,db):
        self.__sum = 0
        self.__list = []
        #初始化函数，配置随机消息及对应权值
        #查询DB
        contentInfos = db.select("ContentInfo",where="valid=1")
        #遍历DB中配置的随机消息,并保存到list
        for contentInfo in contentInfos:
            self.__list.append(contentInfo)
            #计算权值总数
            self.__sum = self.__sum + contentInfo.weight
    
    def getMsg(self):
        #获取0-权值总数之间的任意整数，作为随机值
        currWeight = random.randint(0, self.__sum)
        currSum = 0
        #遍历消息的权值，并累加，当累加值超过随机值时，返回该消息
        for i in range(0, len(self.__list)):
            currSum = currSum + self.__list[i].weight
            if currSum > currWeight:
                return self.__list[i - 1].contentMsg
        return ""



#彩蛋关键字匹配，若成功返回对应消息
class KeyManager(object):
    def __init__(self,db):
        self.__keyInfoList  = []
        #初始化函数，配置关键字信息
        #查询DB
        keyInfos = db.select("KeyInfo",where="valid=1")
        for keyInfo in keyInfos:
            self.__keyInfoList.append(keyInfo)
        
    def getMsg(self,recvContent):
        #遍历关键字，进行匹配
        for keyInfo in self.__keyInfoList:
            if keyInfo.keyWord.decode('unicode-escape') in recvContent.decode('unicode-escape'):
                return keyInfo.contentMsg
        return ""



class NewsManager(object):
    def __init__(self,db):
        self.__db = db
        self.__keyManager = KeyManager(db)
        self.__keyMap = {}
        self.__keyMap["新闻"] = self.getAllNews
        self.__keyMap["猎云网"] = self.getSpecialHostNews
    
    def getMsg(self,usrInfo):
        recvContent = usrInfo.msgContent
        #首先判断是不是数字
        if recvContent.isdigit():
            #如果为数字
            return self.getNewsDetail(recvContent)
        
        #优先遍历新闻关键字
        for (key,value) in self.__keyMap.items():
            if recvContent.decode('unicode-escape') == key.decode('unicode-escape'):
                return value(recvContent,usrInfo)
        #如果没有新闻关键字，尝试遍历彩蛋关键字
        return self.__keyManager.getMsg(recvContent)
        
    def getAllNews(self,recvContent,usrInfo):
        #得到偏移量
        offset = int(usrInfo.getCurTypeOffset(recvContent))
        newsInfos = self.__db.select("NewsInfo",what="id,newsTitle",offset=offset,limit=10,order="id DESC")
        
        #保存最新偏移量
        getCount = len(newsInfos)
        if getCount < 10:
            offset = 0
        else:
            offset += getCount
        usrInfo.setCurTypeOffset(recvContent,offset)

        #遍历读取到的新闻
        content = "全部新闻："
        content = "新闻编号：新闻标题\n"
        for newsInfo in newsInfos:
            content += str(newsInfo.id) + ":" + newsInfo.newsTitle + "\n"
        content += "\n再次输入\"新闻\",获取更多资讯"
        return content
    
    def getNewsDetail(self,recvContent):
        content = ""
        newsInfoList  = []
        strWhere = "id = " + recvContent + " and valid=1"
        newsInfos = self.__db.select("NewsInfo",where=strWhere )
        #将查询到的数据存入list
        for newsInfo in newsInfos:
            newsInfoList.append(newsInfo)
        if len(newsInfoList) != 0:
            content += str(newsInfoList[0].id) + ":" + newsInfoList[0].newsTitle + "\n"
            content += "摘自：" + newsInfoList[0].webName + " " + newsInfoList[0].sectionName + "版块\n\n"
            content += newsInfoList[0].newsSummary + "\n\n"
            content += "详情点击：" + newsInfoList[0].newsUrl 
            return content
        content = "id:" + recvContent + " 对应文章不存在或已删除，请重新输入！"
        return content

    def getSpecialHostNews(self,recvContent,usrInfo):
        #得到偏移量
        offset = int(usrInfo.getCurTypeOffset(recvContent))
        where = "webName = \"" + recvContent + "\""
        newsInfos = self.__db.select("NewsInfo",what="id,newsTitle",offset=offset,limit=10,order="id DESC",where=where)
        
        #保存最新偏移量
        getCount = len(newsInfos)
        if getCount < 10:
            offset = 0
        else:
            offset += getCount
        usrInfo.setCurTypeOffset(recvContent,offset)

        #遍历读取到的新闻
        content = recvContent +":\n"
        content += "新闻编号：新闻标题\n"
        for newsInfo in newsInfos:
            content += str(newsInfo.id) + ":" + newsInfo.newsTitle + "\n"
        content += "\n再次输入\""+ recvContent + "\",获取更多" + recvContent + "资讯"
        return content

