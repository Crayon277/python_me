#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: challenge_2.py
# Created Time: Mon Jun  1 22:58:19 2015

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

msg = []

with open("challenge_2.txt",'r') as fp :
    while(1):
        line = fp.readline()
        if(len(line) == 0):
            break
        for x in line:
            if ord(x) >= ord('a') and ord(x) <= ord('z'):
                msg.append(x)


print msg
