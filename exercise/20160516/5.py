#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: 5.py
# Created Time: Mon May 16 10:33:04 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

#输入三个整数x,y,z，请把这三个数由小到大输出。

dic = {}
maxium = -1

def caozuo(num):
    # dic = {}
    # dic['h'] = 'yes'
    global maxium
    if num > maxium:
        maxium = x
    dic[num] = 'yes'
    # print dic

for i in range(3):
    x = int(raw_input("> "))
    caozuo(x)

for i in range(1,maxium+1):
    if dic.has_key(i):
        print 'p:',i

print "the global dict is",dic
