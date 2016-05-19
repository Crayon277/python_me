#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: 40_reverse_print_array.py
# Created Time: Thu May 19 23:26:18 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

#将一个数组逆序输出。

l = []

while 1:
    try:
        n = int(raw_input())
        l.append(n)
    except EOFError:
        break
print l
for i in l[::-1]:
    print i,


"""
另一个思路，
第一个和最后一个交换

"""
