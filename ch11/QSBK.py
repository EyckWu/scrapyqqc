#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = eyckwu
# coding:utf-8
import urllib2
import urllib
import re
import sys
reload(sys)
sys.setdefaultencoding('utf8')

class QSBK(object):
    def __init__(self):
        self.pageIndex = 1
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.headers = {'User-Agent': self.user_agent}
        # 存放段子的变量，每一个元素是每一页的段子们
        self.stories = []
        # 存放程序是否继续运行的变量
        self.enable = False

    def getPage(self, page):
        url = 'http://www.qiushibaike.com/hot/page/' + str(self.pageIndex)
        try:
            request = urllib2.Request(url, headers=self.headers)
            response = urllib2.urlopen(request)
            content = response.read().decode('utf-8')
            # print(content)
            return content
        except urllib2.URLError, e:
            if hasattr(e, 'code'):
                print(e.code)
            if hasattr(e, 'reason'):
                print(e.reason)

    def getPageItem(self,pageIndex):
        pageCode = self.getPage(pageIndex)
        if not pageCode:
            print("页面加载失败")
            return
        pattern = re.compile('<div class="article.*?<h2>(.*?)</h2>.*?<span>(.*?)</span>', re.S)
        items = re.findall(pattern, pageCode)
        pageStroies = []
        for item in items:
            replaceBR = re.compile('<br/>')
            # print(item[1].strip())
            tmp = re.sub(replaceBR, '\n', item[1])
            item = [item[0].strip(), tmp.strip()]
            pageStroies.append(item)

        return pageStroies

    def loadPage(self):
        if self.enable == True:
            for index in range(1,5):
                pagestroies = self.getPageItem(1)
                self.stories.append(pagestroies)
            # for i in pagestroies:
                # print("***")

            # self.stories.append(self.getPageItem(1))

    def printPage(self, pageStrois, index):
        for stroy in pageStrois:
            print('第%d页\t发布者：%s\n内容：%s\n' % ( index , stroy[0], stroy[1]))
            # print(stroy[1])

    def start(self):
        self.enable = True
        self.loadPage()
        i = 1
        for s in self.stories:
            self.printPage(s,i)
            i += 1

qsbk = QSBK()
qsbk.start()