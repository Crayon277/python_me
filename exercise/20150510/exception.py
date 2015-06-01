#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: exception.py
# Created Time: Mon May 11 09:00:26 2015

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

def foo(s):
    return 10/s

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except StandardError,e:
        print "ValueError",e
    else:
        print "Some Error happen"
    finally:
        print 'bar() fails'
    print 'END of Func'

main()

