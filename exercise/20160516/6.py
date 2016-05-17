#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: 6.py
# Created Time: Mon May 16 11:22:01 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

#斐波那契数列

x = 10

f1 = 0
f2 = 1

for i in range(10):
    print f1
    f2 = f1 + f2
    f1 = f2 - f1

