#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: test_print_lol.py
# Created Time: Wed Sep  7 06:49:19 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

from print_lol import print_lol

mlist = []

for i in range(10):
    mlist.append(i)

test = open('test.txt','w')

print_lol(mlist,out=test)
