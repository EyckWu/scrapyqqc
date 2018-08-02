#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = eyckwu

import urllib2
import cookielib

filename = 'cookie.txt'
#声明一个CookieJar对象实例来保存cookie
cookie = cookielib.MozillaCookieJar(filename)
#利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)
request = urllib2.Request('http://www.baidu.com')
response = opener.open(request)
for item in cookie:
    print('name==' + item.name)
    print('value==' + item.value)

cookie.save(ignore_discard = True, ignore_expires = True)