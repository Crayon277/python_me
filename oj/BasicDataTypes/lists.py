#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: lists.py
# Created Time: Wed Sep 14 17:28:08 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

l=[]
for _ in range(int(raw_input())):
    order = raw_input().strip().split()
    if order[0] == 'insert':
        l.insert(int(order[1]),int(order[2]))
        continue
    if order[0] == 'print':
        print l
        continue
    if order[0] == 'remove':
        l.remove(int(order[1]))
        continue
    if order[0] == 'append':
        l.append(int(order[1]))
        continue
    if order[0] == 'sort':
        l.sort()
        continue
    if order[0] == 'pop':
        l.pop()
        continue
    if order[0] == 'reverse':
        l.reverse()
        continue




