#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: 19_WanShu_v2.py
# Created Time: Tue May 17 18:06:39 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

from sys import stdout

for j in range(2,1001):
    k = []
    n = -1
    s = j
    for i in range(1,j):
        if j %i == 0:
            n += 1
            s -= i
            k.append(i)
    if s==0: #它使用减法，零就是两者相等了
        print j
        print 'n =',n
        print 'range(n) = ',range(n)
        for i in range(n): #对的，我奇怪为什么n从-1开始这里还range(n), 最后还要print k[n]
            stdout.write(str(k[i]))
            stdout.write(' ')
        print k[n]


