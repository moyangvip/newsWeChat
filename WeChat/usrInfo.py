# -*- coding: utf-8 -*-
# filename: usrInfo.py
import memcache

mc = memcache.Client(['127.0.0.1:11333'],debug=0)

class UsrInfo(object):
    def __init__(self):
        self.usrId = ""  #该用户的id
        self.appId = ""   #该订阅号id
        self.msgType = "" #该用户当前的消息类型
        self.msgContent = ""  #该用户当前的发送消息
        self.lastType = ""    #该用户上次请求新闻类型
        self.lastOffset = "0"     #上次请求类型的偏移量

    def init(self,recMsg):
        self.usrId = recMsg.FromUserName  #该用户的id
        self.appId = recMsg.ToUserName   #该订阅号id
        self.msgType = recMsg.MsgType #该用户当前的消息类型
        self.msgContent = recMsg.Content.strip()  #该用户当前的发送消息

    def setCurTypeOffset(self,currType,currOffset):
        strOffset = str(currOffset)
        key = "MT_" + self.usrId + "_" + str(hash(currType))
        #默认只存1分钟
        mc.set(key.encode("utf-8"),strOffset,time=60)
        print "set offset:" ,strOffset
        self.lastType = currType
        self.lastOffset = strOffset
    
    def getCurTypeOffset(self,currType):
        key = "MT_" + self.usrId + "_" + str(hash(currType))
        strOffset = mc.get(key.encode("utf-8"))
        if strOffset == None:
            self.lastPage = "0"
            return self.lastPage
        self.lastOffset = strOffset
        print "get offset:" ,strOffset
        return strOffset


