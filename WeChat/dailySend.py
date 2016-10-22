# -*- coding: utf-8 -*-
# filename: dailySend.py
# 用于每日推送，当前订阅号权限不够，当前未用到，TODO
import urllib
import time
import json
from datetime import datetime,date
class Timer:
    def __init__(self):
        self.__week_day_dict = {
          0 : '星期一',
          1 : '星期二',
          2 : '星期三',
          3 : '星期四',
          4 : '星期五',
          5 : '星期六',
          6 : '星期天',
        }

    #获取今天周几
    def get_week_day(self,date):
        day = date.weekday()
        return self.__week_day_dict[day]

    #TODO 特殊日子推送内容
    def getSpecialDayMsg(self,date):
        return (False,time(0, 0, 0),"")

    #正常推送内容
    def getCommonDayMsg(self,date):
        weekend = [5,6]
        #获取星期数
        dayOfWeek = date.weekday()
        #如果为周末
        if dayOfWeek in weekend:
            content = "今天是",date.strftime('%b年%d月%日'),",",get_week_day(date),"周末啦，黄阿姨早安~"
            return (time(9, 0, 0),content)
        leftDay = 5 - dayOfWeek
        content = "今天是",date.strftime('%b年%d月%日'),",",get_week_day(date),"，离周末还有",leftDay,"天，黄阿姨早安~"
        return (time(7, 0, 0),content)
    #TODO
    def sendMsg(self,content):
        pass