#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: 39_insert_in_sorted_array.py
# Created Time: Thu May 19 23:16:34 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

#一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。


l=[1,3,5,7,9]

n = int(raw_input())
flag = 0
for i in range(len(l)):
    if l[i] > n:
        idx = i
        flag = 1
        break

print l
print 'insert %d'%n
if flag:
    l.insert(idx,n)
else:
    l.append(n)
print l
