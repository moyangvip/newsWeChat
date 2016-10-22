# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals
from bosonnlp import BosonNLP

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
#最大字数
WORD_LIMIT = 300

class Summary(object):
    def __init__(self):
        # 我申请的API Token
        self.__nlp = BosonNLP('JM1QZck5.9720.Kk6SbRPkfMsz')
    
    def getSummary(self,title,content):
        # 完整的参数调用如下：
        # result = nlp.summary(title, content, word_limit=0.3, not_exceed=0)
        # 修改标题为该文章标题，如下：
        # title = '前优酷土豆技术副总裁黄冬加盟芒果TV任CTO'
        # result = nlp.summary(title, content, word_limit=0.3, not_exceed=0)
        # 修改word_limit选项为百分之二十，如下：
        # result = nlp.summary(title, content, word_limit=0.2, not_exceed=0)
        # 修改word_limit选项为具体字数200时，如下：
        # result = nlp.summary(title, content, word_limit=200, not_exceed=0)
        # 修改no_exceed选项为严格不超出字数限制时，如下：
        # result = nlp.summary(title, content, word_limit=0.3, not_exceed=1)
        # 当前设置为摘要字数不能超过300字
        result = self.__nlp.summary(title, content,WORD_LIMIT,0)
        # 摘要内容不换行
        result = result.replace("\n","")
        return result