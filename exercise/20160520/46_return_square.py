#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: 46_return_square.py
# Created Time: Fri May 20 10:23:51 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

#输入数字，返回平方，如果数字小于50推出程序


while 1:
    n = int(raw_input("> "))
    if n < 50:
        break
    else:
        print n**2
