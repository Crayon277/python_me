#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: lists_nb.py
# Created Time: Wed Sep 14 17:39:32 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

l =[]

for _ in range(input()):
    order = raw_input().spilt()
    cmd = order[0]
    args = order[1:]
    if cmd != 'print':
        cmd += "("+','.join(args)+')'
        eval('l.'+cmd)
    else:
        print l

#我之所以不会用eval是没有意识到，里面的参数，其实就是对字符串的处理！！！！
#对字符串处理将其生成命令
    
