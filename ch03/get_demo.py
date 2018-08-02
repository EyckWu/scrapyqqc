#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = eyckwu

import urllib
import urllib2

values = {}
values['username'] = "eyck"
values['password'] = "123456"
data = urllib.urlencode(values)
url = "http://passport.csdn.net/account/login"
getUrl = url + "?" + data
request = urllib2.Request(getUrl)
response = urllib2.urlopen(request)
print(response.read())