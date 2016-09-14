#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: download_test.py
# Created Time: Sun Sep  4 22:05:16 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

import urllib2

f=urllib2.urlopen('http://www.runoob.com/python/python-exercise-example64.html')
file_save = open('test.html','w')
file_save.write(f.read())
file_save.close()


