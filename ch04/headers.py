#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = eyckwu

import urllib2
import urllib

url = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
referer = 'http://www.zhihu.com/articles'
headers = {'User-Agent': user_agent, 'Referer':referer}
values = {'username':'eyck','password':'12345'}
data = urllib.urlencode(values)
request = urllib2.Request(url, data, headers)
response = urllib2.urlopen(request)
page = response.read()
print(page)