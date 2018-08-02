#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = eyckwu

import urllib2
import urllib
import cookielib

filename = 'cookie.txt'
headers = {
    'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
    'Referer':'https://ssp.scnu.edu.cn/Default.aspx',
    'Origin':'https://ssp.scnu.edu.cn',
    'Cookie':'ASP.NET_SessionId=50ivrwhqj0tqfijuxlsh12h0; UM_distinctid=1643a35732f166-0e88e98741042f-47e1137-1fa400-1643a357333269',
    'Host':'ssp.scnu.edu.cn',
    'Upgrade-Insecure-Requests':'1',
    'Content-Type':'application/x-www-form-urlencoded',
    'Accept-Language':'zh-CN,zh;q=0.9',
    # 'Accept-Encoding':'gzip, deflate, br',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
}
cookie = cookielib.MozillaCookieJar(filename)
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
data = urllib.urlencode({
    'ctl00$cph_default$log_username':'20143100044',
    'ctl00$cph_default$log_password':'W15889118762',
    'ctl00$cph_default$logon':'本地登录',
    '__VIEWSTATEGENERATOR':'CA0B0334',
    '__EVENTVALIDATION':'/wEdAARLWJN6vqW1dZ8nzu5y2EwDiEsaCn2l/df20Jj1uQ6TeDesOwbVQRHP0Xvs0jqbyaqLIOOWmS94+eQYeCG5lthMad3mtR+yXGyWNKhJjXGqackEQhF7L1BIghjR7A26AIw='
})
loginurl = 'https://ssp.scnu.edu.cn/Default.aspx'
request = urllib2.Request(loginurl, data,headers)
response = opener.open(request)
# print(request.headers)
# print(request.data)
result = response.read()
print(result)

print("***********")
cookie.save(ignore_discard=True, ignore_expires=True)
# gradeurl = 'https://ssp.scnu.edu.cn/opt_jy_jydj.aspx?key=n9Q4ISC401kEohqh&fid=129'
# response = opener.open(gradeurl)
# print(response.read())