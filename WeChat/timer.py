# -*- coding: utf-8 -*-
# filename: timer.py
# 用于定制定时事件，用于主动推送服务，当前权限不够，当前未用到，TODO
import urllib
import time
import json
from datetime import datetime,date

class Timer:
    def __init__(self):
        self.__appId = "wx1ca29b50eb95daeb"
        self.__appSecret = "a642fb96788a7774fcb701e1515248fc"
        #主动发送消息需要用到的token码
        self.__accessToken = ''
        #accessToken的存活时间，一般为2小时
        self.__leftTime = 0

    #请求获取token码
    def get_access_token(self):
        postUrl = ("https://api.weixin.qq.com/cgi-bin/token?grant_type="
               "client_credential&appid=%s&secret=%s" % (self.__appId, self.__appSecret))
        urlResp = urllib.urlopen(postUrl)
        urlResp = json.loads(urlResp.read())
        
        self.__accessToken = urlResp['access_token']
        self.__leftTime = urlResp['expires_in']
    

    #定时器轮询...TODO
    def loop(self):
        date = datetime.now()
        while(True):
            current_time = time.localtime(time.time())
            return ""