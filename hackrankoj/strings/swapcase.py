#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: swapcase.py
# Created Time: Fri Sep 16 21:10:32 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

#最简单的
print raw_input().swapcase()

#运用join，字符串 
print ''.join([i.lower() if i.isupper() else i.upper() for i in raw_input()])

