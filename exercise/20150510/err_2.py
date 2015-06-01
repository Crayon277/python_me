#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: err_2.py
# Created Time: Mon May 11 10:07:46 2015

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'
import logging
logging.basicConfig(level = logging.INFO)

def foo(s):
    n = int(s)
 #   assert n!=0,'n is zero'
    logging.info('n = %d'%n)

    return 10/n


def bar(s):
    try:
        return foo(s)*2
    except StandardError,e:
        print 'Error'
        raise
def main():
    bar('0')

main()

print 'if print'
