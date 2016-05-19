#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: 32_reverse_print_list.py
# Created Time: Thu May 19 15:29:03 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

#按相反的顺序输出列表的值。

l=[]

while 1:
    try:
        n = int(raw_input(">"))
        l.append(n)
    except EOFError:
        break

print 'original list',l
l.reverse()
print 'reverse list',l



