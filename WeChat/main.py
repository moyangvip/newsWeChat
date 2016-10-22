# -*- coding: utf-8 -*-
# filename: main.py
import web
import sys
from handle import Handle
#设置规则，当请求后缀为/wx,将调用Handle模块
urls = (
    '/wx', 'Handle',
)
#设置默认编码为utf8
reload(sys)
sys.setdefaultencoding( "utf-8" )
#实际main函数入口，启动服务器
if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()
