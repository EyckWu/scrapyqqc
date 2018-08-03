#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = eyckwu

import re
# c = r'(\w+) (\w+)'
# pattern = re.compile(r'(\w+) (\w+)(?P<sign>.*)')
pattern = re.compile(r'(\w+) (\w+)')
m = re.match(pattern, 'hello python hh hello re')
m = re.search(pattern, 'hello python hh hello re')
m = re.findall(pattern, 'hello python hh hello re')
m = re.finditer(pattern, 'hello python hh hello re')

for i in m:
    print(i.group())
# print m[1]
# print "m.string:", m.string
# print "m.re:", m.re
# print "m.pos:", m.pos
# print "m.endpos:", m.endpos
# print "m.lastindex:", m.lastindex
# print "m.lastgroup:", m.lastgroup
# print "m.group():", m.group()
# print "m.group(1,2):", m.group(1,2)
# print "m.groups():", m.groups()
# print "m.groupdict():", m.groupdict()
# print "m.start(2):", m.start(2)
# print "m.end(2):", m.end(2)
# print "m.span(2):", m.span(2)
# print r"m.expand(r'\g \g\g'):", m.expand(r'\2 \1\3')

# m.string: hello python
# m.re: <_sre.SRE_Pattern object at 0x00000000027E8250>
# m.pos: 0
# m.endpos: 12
# m.lastindex: 3
# m.lastgroup: sign
# m.group(): hello python
# m.group(1,2): ('hello', 'python')
# m.groups(): ('hello', 'python', '')
# m.groupdict(): {'sign': ''}
# m.start(2): 6
# m.end(2): 12
# m.span(2): (6, 12)
# m.expand(r'\g \g\g'): python hello