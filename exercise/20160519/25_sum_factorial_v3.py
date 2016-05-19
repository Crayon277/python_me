#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: 25_sum_factorial_v3.py
# Created Time: Thu May 19 10:23:55 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

#求1+2!+3!+...+20!的和。

from math import factorial

l = []

for i in range(1,21):
    l.append(factorial(i))

print reduce(lambda x,y:x+y,l)

