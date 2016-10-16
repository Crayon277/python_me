#!/usr/bin/python
#-*- coding: utf-8 -*-
from collections import defaultdict
d=defaultdict(list)
a,b=map(int,raw_input().split())
for index in range(a):
    d[raw_input()].append(index+1)
#print d
for _ in range(b):
    value = raw_input()
    if value in d:
        print ' '.join(map(str,d[value]))
    else:
        print -1

'''
for _ in range(b):
    print ' '.join(map(str,d[raw_input()])) or -1


利用这个特性
So if key 'x' is not present in d = defaultdict(list) and I try to execute d['x'],
I will get an empty list but an ordinary dictionary would return me a keyvalue error.
'''
