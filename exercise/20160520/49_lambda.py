#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: 49_lambda.py
# Created Time: Fri May 20 11:04:46 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

#使用lambda来创建匿名函数。


maximum = lambda x,y:(x>y)*x +(x<y)*y
minimum = lambda x,y:(x>y)*y +(x<y)*x

if __name__ == '__main__':
    a = 10
    b = 20 
    print 'The larger one is %d'%maximum(a,b)
    print 'The smaller one is %d'%minimum(a,b)

