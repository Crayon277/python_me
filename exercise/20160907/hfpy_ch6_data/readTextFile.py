#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: readTextFile.py
# Created Time: Thu Sep  8 23:35:19 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

fname = raw_input('enter file name:')
print 

try:
    f = open(fname)
except IOError as err:
    print 'file error' + err
else:
    for line in f.readlines():
        line = line.strip('\n')
        print line
    f.close()
