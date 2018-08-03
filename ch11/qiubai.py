#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = eyckwu

import urllib
import urllib2
import re

page = 1
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
try:
    request = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(request)
    content = response.read().decode('utf-8')
    print(content)
    pattern = re.compile('<div class="article.*?<h2>(.*?)</h2>.*?<span>(.*?)</span>',re.S)
    items = re.findall(pattern, content)
    for item in items:
        print(item[0])
        print(item[1])
    # print(response.read())
except urllib2.URLError, e:
    if hasattr(e,'code'):
        print(e.code)
    if hasattr(e, 'reason'):
        print(e.reason)