#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: 26_recursion.py
# Created Time: Thu May 19 10:44:55 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

#利用递归方法求5!。


def recursion(n):
    if n == 1:
        return 1
    else:
        return n*recursion(n-1)

print recursion(5)

