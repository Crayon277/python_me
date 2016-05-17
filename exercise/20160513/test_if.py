#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: test_if.py
# Created Time: Fri May 13 16:06:01 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

from sys import exit
def foo(x):
    if x < 10:
        print '100'
    elif x < 20:
        print '50'
    elif x <30:
        print "10"
    else:
        print '0'
while 1:
    try:
        test = int(raw_input('> '))
    except EOFError:
        print 'let\'s go'
        exit(0)
    foo(test)


