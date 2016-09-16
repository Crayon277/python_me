#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: list_comprehensive_v2.py
# Created Time: Fri Sep 16 08:35:47 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

#avoid set and sort!

n = input()
lis = list(map(int,raw_input().split()))
m = max(lis)

#max 如果不用内建函数
m = reduce(lambda x,y:x if x > y else y,lis)

while max(lis) == m:
    lis.remove(m)
#关键在这里，remove掉所有原本最大的。剩下最大的就是原本第二大了。
print max(lis)
    

#还有一种
a = sorted(list(map(int,raw_input().split())))
w = a.index(max(a))
#利用index的特性！！！返回第一个出现的值的索引
print a[w-1]
