#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: what_happen_if_have_two_same_function_def.py
# Created Time: Thu Nov  3 17:51:28 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

def test():
    print 'this is the first test'


def test():
    print 'this is the second test'

test()
