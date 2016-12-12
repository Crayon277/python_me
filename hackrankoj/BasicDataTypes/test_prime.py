#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: test_prime.py
# Created Time: Fri Sep 16 18:14:23 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'
import math
def prime(num):
    for i in range(2,int(math.sqrt(num)+1)):
        if num % i == 0:
            return False
    return True

print prime(input())
