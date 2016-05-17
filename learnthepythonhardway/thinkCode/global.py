#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: global.py
# Created Time: Tue May 10 21:50:19 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

def func():
    global x
    print "x is ",x
    x = 2
    print "change x to",x

x = 50
func()
print "x = ",x

