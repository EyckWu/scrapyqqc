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
        return item.group(1).strip()

    def getItemCount(self, page):
        pattern = re.compile(r'<li class="l_reply_num" style="margin-left:8px" >.*?class="red">(.*?)</span>', re.S)
        item = re.search(pattern, page)
        print(item.group(1).strip())
        return item.group(1).strip()

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
            self.file = open(self.defaultTitle + '.txt', 'w+')

    def writeData(self, contents):
        for item in contents:
            if self.floorTag == '1':
                # 楼之间的分隔符
                floorLine = "\n" + str(
                    self.floor) + u"-----------------------------------------------------------------------------------------\n"
                self.file.write(floorLine)
            self.file.write(item)
            self.floorTag += 1

    def start(self):
        indexPage = self.getPage(1)
        pageNum = self.getItemCount(indexPage)
        pageTitle = self.getTitle(indexPage)
        self.setTitle(pageTitle)
        if pageNum == None:
            print ('请重试')
            return
        print('该帖子共有%d页帖子' % int(pageNum))
        try:
            for i in range(1, (int)(pageNum) + 1):
                print ('正在写入第%d页数据' % i)
                page = self.getPage(i)
                contents = self.getContent(page)
                self.writeData(contents)
            print('数据写入完毕')
        except IOError, e:
            print e.message

baseUrl = 'http://tieba.baidu.com/p/3138733512'
bdtb = BDTB(baseUrl, 1, 1)
bdtb.start()
# page = bdtb.getPage(1)
# bdtb.getTitle(page)
# bdtb.getItemCount(page)
# bdtb.getContent(page)

