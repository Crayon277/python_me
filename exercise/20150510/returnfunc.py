#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: returnfunc.py
# Created Time: Sun May 10 17:24:03 2015

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

def func(x):
    f = []
    for i in x:
        def fn(j):
            def gn():
                return j*j
            return gn
        f.append(fn(i))
    return f

l = [1,2,3]
x,y,z = func(l)

print x()
print y()
print z()
