#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: 8.py
# Created Time: Mon May 16 14:12:13 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

for i in range(1,10):
    for j in range(1,i):
        print ' '*6, #,是为了输出格式好看，注意,在输出会自动又一个空格
    for j in range(i,10):
        print '%d*%d=%2d'%(i,j,i*j),
    print '\n' 
