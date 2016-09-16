#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: list_comprehensive_v2.py
# Created Time: Fri Sep 16 08:35:47 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

#avoid set and sort!

n = input()
lis = list(map(int,raw_input().split()))
m = max(lis)

while max(lis) == m:
    lis.remove(m)
#关键在这里，remove掉所有原本最大的。剩下最大的就是原本第二大了。
print max(lis)
    
