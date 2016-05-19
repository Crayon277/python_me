#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: 25_sum_factorial_v2.py
# Created Time: Thu May 19 09:49:46 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'


#求1+2!+3!+...+20!的和。

#map 的用法

import math

l = range(1,21)

print sum(map(math.factorial,l))


