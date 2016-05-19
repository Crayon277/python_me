#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: 36_prime_in_100.py
# Created Time: Thu May 19 16:17:20 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

#求100之内的素数。

from math import sqrt

def if_prime(n):
    flag = 0
    # for i in range(2,int(sqrt(n+1))): 这个判断的话，4就会判为素数，因为int(sqrt(4+1)) = 2 ,range(2,2)其实没有进入循环
    for i in range(2,int(sqrt(n))+1):
        if n % i == 0:
            flag =1
    if flag:
        return False
    else:
        return True

# print if_prime(4)

for i in range(1,100):
    if i == 1 or i == 2:
        print i
        continue
    if if_prime(i):
        print i
