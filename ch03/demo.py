#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = eyckwu

import urllib2

# response = urllib2.urlopen("http://www.baidu.com")
request = urllib2.Request("http://www.baidu.com")
response = urllib2.urlopen(request)
print(response.read())