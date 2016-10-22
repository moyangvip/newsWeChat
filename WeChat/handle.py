# -*- coding: utf-8 -*-
# filename: handle.py
# 接收消息的核心处理类
import hashlib
import reply
import receive
import web
from msgManager import DefaultManager
from msgManager import NewsManager
from usrInfo import UsrInfo

#连接数据库
db = web.database(dbn='mysql', db='WeChatDB', user='root', pw='123456')
#初始化消息内容处理对象
defaultManager = DefaultManager(db)
newsManager = NewsManager(db)

class Handle(object):
    # 收到post方式的请求
    def POST(self):
        try:
            #获取收到的消息
            webData = web.data()
            #对接收到的消息进行解析
            recMsg = receive.parse_xml(webData)
            #初始化用户对象
            usrInfo = UsrInfo()
            usrInfo.init(recMsg)
            if isinstance(recMsg, receive.Msg):
                #收到的为文字信息
                if recMsg.MsgType == 'text':
                    #打印日志
                    print "Time:",recMsg.CreateTime,"From:",recMsg.FromUserName," Get msg:",recMsg.Content
                    #尝试关键字匹配
                    content = newsManager.getMsg(usrInfo)
                    if content == "":
                        #关键字匹配失败，进行随机返回
                        content = defaultManager.getMsg()
                    #将待发送消息格式化
                    replyMsg = reply.TextMsg(usrInfo.usrId, usrInfo.appId, content)
                #收的的为图片信息
                if recMsg.MsgType == 'image':
                    content = "当前无法识别图片信息"
                    replyMsg = reply.TextMsg(usrInfo.usrId, usrInfo.appId, content)
                #发送返回消息
                return replyMsg.send()
            else:
                print "暂且不处理"
                return "success"
        except Exception, Argment:
            print "异常：",Argment
            return "success"