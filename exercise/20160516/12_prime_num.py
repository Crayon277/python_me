#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: prime_num.py
# Created Time: Mon May 16 17:02:19 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

#判断101-200之间有多少个素数，并输出所有素数。

import math

def if_prime(num):
    top = int(math.sqrt(num+1))
    flag = 0
    for i in range(2,top+1):
        if num % i == 0:
            flag = 1#刚写成了flag == 1
            break
    if flag:
        return False
    else:
        return True

for i in range(101,201):
    if if_prime(i):
        print i
