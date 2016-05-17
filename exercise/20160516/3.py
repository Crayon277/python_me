#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: 3.py
# Created Time: Mon May 16 09:12:05 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

#一个整数，它加上100和加上268后都是一个完全平方数，请问该数是多少？

pingfang = [x**2 for x in range(100)]

for item in pingfang:
    if item+168 in pingfang:
        print item-100

