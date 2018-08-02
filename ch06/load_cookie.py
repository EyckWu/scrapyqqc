#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = eyckwu

import cookielib
import urllib2

url = 'https://ssp.scnu.edu.cn/Default.aspx'


cookie = cookielib.MozillaCookieJar()
cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
request = urllib2.Request('https://ssp.scnu.edu.cn/Default.aspx')
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
response = opener.open(request)
print(response.read())