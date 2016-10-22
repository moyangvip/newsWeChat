# -*- coding: utf-8 -*-
# filename: test.py
 
import memcache
import sys
#设置默认编码为utf8
reload(sys)
sys.setdefaultencoding( "utf-8" )

mc = memcache.Client(['127.0.0.1:11333'],debug=0)
key = "中文"
key = str(hash(key))
print key
mc.set(key,"bar",time=60)
mc.set(key,"bar2",time=60)
value = mc.get(key)
print value