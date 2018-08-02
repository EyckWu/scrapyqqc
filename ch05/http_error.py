#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = eyckwu

import urllib2
request = urllib2.Request('http://blog.csdn.net/cqcre')
try:
    response = urllib2.urlopen(request)
except urllib2.HTTPError, e:
    print(e.code)
    print(e.reason)
else:
    print(response.read())