#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: 68_v2.py
# Created Time: Mon Sep  5 10:26:16 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

#题目：有n个整数，使其前面各数顺序向后移m个位置，最后m个数变成最前面的m个数


def move(array,n,m):
    array_end = array[n-1]
    for j in range(n-1,-1,-1):
        array[j] = array[j-1]
    array[0] = array_end
    m-=1
    if m>0:
        move(array,n,m)

