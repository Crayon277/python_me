#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: 54_extract_4_7_bit.py
# Created Time: Fri May 20 12:29:47 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

#取一个整数a从右端开始的4〜7位。


a = int(raw_input())

b = a>>4
c = ~(~0<<4)
print b
print c
d = b&c
print '%x'%d
