#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: 69_n_baoshu.py
# Created Time: Mon Sep  5 12:25:27 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

#题目：有n个人围成一圈，顺序排号。从第一个人开始报数（从1到3报数），凡报到3的人退出圈子，问最后留下的是原来第几号的那位。

sequence = []
for i in range(1,13):
    sequence.append(i)

index = 0
baoshu = 0
while len(sequence)>1:
    if baoshu == 2:
        sequence.remove(sequence[index])
    else:
        index=(index+1)%(len(sequence))
    baoshu = (baoshu+1)%3

print sequence[0]
