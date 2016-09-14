#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: 47_exchange_two_var.py
# Created Time: Fri May 20 10:36:22 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

#两个变量值互换。

a = 1
b = 2

print 'a=',a
print 'b=',b

a,b = b,a
"""
a=a+b
b=a-b
a=a-b
"""

"""
a=a^b
b=a^b #这时b=a其实是a^b^b, b^b=0，0^任何＝任何本身
a=a^b #这时相当于 a^b^a

"""
print 'a=',a
print 'b=',b
