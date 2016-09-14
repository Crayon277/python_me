#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: 65_sorted_output.py
# Created Time: Sun Sep  4 22:40:23 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'


a=int(input('enter a num:'))
b=int(input('enter b num:'))
c=int(input('enter c num:'))

def cmp(x,y):
    print '===inside:'
    print x,y
    if x < y:
        x=x+y
        y=x-y
        x=x-y
    else:
        pass
    print 'after:'
    print x,y
    print 'over===='
    return x,y

def cmp2(x,y):
    if x<y:
        return y,x
    else:
        return x,y

a,b=cmp(a,b)
print a,b
a,c=cmp(a,c)
print a,c
b,c=cmp(b,c)
print b,c

print a,b,c
