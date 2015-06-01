#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: with_module_test.py
# mail: mmmmmcclxxvii@gmail.com
# Created Time: Sun May 10 15:23:33 2015

__author__ = 'Crayon Chaney'

import sys

def test():
    args = sys.argv
    if len(args) == 1:
        print "hello world"
    elif len(args) == 2:
        print "hello , %s"%args[1]
    else:
        print "Too many arguments"

if __name__ == "__main__":
    test()

