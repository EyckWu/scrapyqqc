#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = eyckwu

import re

pattern = re.compile(r'hello')
#match返回一个字符数组['h','e','l','l','o']
result1 = re.match(pattern, 'hello')
result2 = re.match(pattern, 'hello eyck')
result3 = re.match(pattern, 'helo eyck')
result4 = re.match(pattern, 'helloo eyck')

if result1:
    print(result1.group())
else:
    print("result1匹配失败")

if result2:
    print(result2.group())
else:
    print("result2匹配失败")

if result3:
    print(result3.group())
else:
    print("result3匹配失败")

if result4:
    print(result4.group())
else:
    print("result4匹配失败")