#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: 48_compare.py
# Created Time: Fri May 20 10:54:21 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

#数字比较



def less():
    print 'less'
    return True

def bigger():
    print 'bigger'
    return True

a = 10
b = 20
(a-b < 0) and less() or bigger()
