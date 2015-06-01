#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: test.py
# Created Time: Mon May 11 09:12:59 2015

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

import os,sys,time

current = os.listdir('.')

all = []

for i in current:
    if not os.path.isfile(i):
        continue
    f = file(i)
    all.append(i)
    while 1:
        content = f.readline()
        if len(content) == 0:
            break
        print content
    f.close()

print all

