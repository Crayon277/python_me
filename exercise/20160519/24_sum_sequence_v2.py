#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: 24_sum_sequence_v2.py
# Created Time: Thu May 19 09:43:09 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

#有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。


dividend = 2.0
divisor = 1.0

l=[]

for i in range(20):
    l.append(dividend/divisor) #这个要放在下面一句的前面
    dividend,divisor = dividend+divisor,dividend
    #因为首项应该是2/1

print reduce(lambda x,y:x+y,l)

