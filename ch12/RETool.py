#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = eyckwu

import re

class Tool(object):
    # 去除img标签,7位长空格
    removeImg = re.compile('<img.*?>| {7}')
    #去除超链接
    removeAddr = re.compile('<a.*?>|</a>')
    #把换行的标签换成\n
    replaceLine = re.compile('<tr>|<div>|</div>|</p>')
    #把表格制表<td>替换\t
    replaceTD = re.compile('<td>')
    #把段落开头替换为\n加两个空格
    replacePara = re.compile('<p.*?>')
    #把换行符或双换行符换成\n
    replaceBR = re.compile('<br><br>|<br>')
    #剔除其他标签
    removeTag = re.compile('<.*?>')
    def replace(self, x):
        x = re.sub(self.removeImg, '', x)
        x = re.sub(self.removeAddr, '', x)
        x = re.sub(self.replaceLine, '', x)
        x = re.sub(self.replaceLine, '\n', x)
        x = re.sub(self.replaceTD, '\t', x)
        x = re.sub(self.replacePara, '\n', x)
        x = re.sub(self.replaceBR, '\n', x)
        x = re.sub(self.removeTag, '', x)
        x = x.strip()
        return x