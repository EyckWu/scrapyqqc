#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = eyckwu
import re
import urllib
import urllib2

url = 'https://blog.csdn.net/zhwadezh/article/details/79111348'
request = urllib2.Request(url)
response = urllib2.urlopen(request)
# print(response.read().decode('utf-8'))
result = response.read().decode('utf-8')
# result = '<h1 class="title-article">Android NFC开发详细总结</h1><h1 class="title-article">Android NFC开发详细总结</h1>'

pattern = re.compile('"title-article">(.*?)</h1>.*?<span class="time">(.*?)</span>',re.S)
items = re.findall(pattern, result)
for item in items:
    print(item[0] + item[1])