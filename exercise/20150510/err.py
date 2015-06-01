#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: err.py
# Created Time: Mon May 11 09:59:29 2015

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

import logging

class FooError(StandardError):
    pass



def foo(s):
    if int(s) == 0:
        raise FooError('invalid value: %s' %s)
    return 10/int(s)

def bar(s):
    return foo(s)*2

def main():
    try:
        bar('0')
    except FooError , e:
        logging.exception(e)

main()
print "end"
