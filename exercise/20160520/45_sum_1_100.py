#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: 45_sum_1_100.py
# Created Time: Fri May 20 10:14:28 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'


#统计 1 到 100 之和。
sum=0
for i in range(1,101):
    sum +=i

print sum

l=[x for x in range(1,101)]
print reduce(lambda x,y:x+y,l)

print (1+100)*100/2.0

