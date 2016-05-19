#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: 25_sum_factorial.py
# Created Time: Thu May 19 09:47:07 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

#求1+2!+3!+...+20!的和。

def factorial(n):
    if n == 1:
        return 1
    else: 
        return n*factorial(n-1)

sum = 0
for i in range(1,21):
    sum += factorial(i)

print sum
