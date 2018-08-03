#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = eyckwu
import urllib2
import urllib
import re
from RETool import Tool

class BDTB(object):
    def __init__(self, baseUrl, seeLZ, floorTag):
        self.baseUrl = baseUrl
        self.seeLZ = '?see_lz=' + str(seeLZ)
        self.tool = Tool()
        self.file = None
        self.floor = 1
        self.defaultTitle = u'百度贴吧'
        self.floorTag = floorTag

    def getPage(self, num):
        try:
            url = self.baseUrl + self.seeLZ + '&pn=' + str(num)
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            page = response.read().decode('utf-8')
            # print(page)
            return page
        except urllib2.HTTPError, e:
            if hasattr(e, 'reason'):
                print(e.reason)
                return None

    def getTitle(self, page):
        pattern = re.compile(r'<h3 class="core_title_txt.*?>(.*?)</h3>',re.S)
        item = re.search(pattern, page)
        print(item.group(1).strip())

    def getItemCount(self, page):
        pattern = re.compile(r'<li class="l_reply_num" style="margin-left:8px" >.*?class="red">(.*?)</span>', re.S)
        item = re.search(pattern, page)
        print(item.group(1).strip())

    def getContent(self, page):
        pattern = re.compile(r'<div id="post_content.*?">(.*?)</div>', re.S)
        items = re.findall(pattern, page)
        contents = []
        for item in items:
            content = '\n' + self.tool.replace(item) + '\n'
            contents.append(content.encode('utf-8'))
            # print('********')
            # print(self.tool.replace(item))
        # print(self.tool.replace(items[1]))
        return contents

    def setTitle(self, title):
        if title is not None:
            self.file = open(title + '.txt', 'w+')
        else:
            self.file = open(self.default + '.txt', 'w+')

    def writeData(self, contents):
        for item in contents:
            print(item)

baseUrl = 'http://tieba.baidu.com/p/3138733512'
bdtb = BDTB(baseUrl, 1, 'hhh')
page = bdtb.getPage(1)
bdtb.getTitle(page)
bdtb.getItemCount(page)
bdtb.getContent(page)

