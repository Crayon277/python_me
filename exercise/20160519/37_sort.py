#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: 37_sort.py
# Created Time: Thu May 19 22:15:41 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

#对10个数进行排序。


# l = [4,6,3,7,11,18,9,3,5,1,10,7]
# sorted_l=[]

l=[]

while 1:
    try:
        n = int(raw_input())
        l.append(n)
    except EOFError:
        break
print l
leng = len(l)

for i in range(leng-1):
    for j in range(leng-1-i):
        if l[j] > l[j+1]:
            l[j] = l[j+1]+l[j]
            l[j+1] = l[j] - l[j+1]
            l[j] = l[j]  - l[j+1]

print l

