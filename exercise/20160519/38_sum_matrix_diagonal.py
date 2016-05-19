#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: 38_sum_matrix_diagonal.py
# Created Time: Thu May 19 22:51:18 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

#求一个3*3矩阵对角线元素之和。
l=[[],[],[]]
sum = 0
for i in range(3):
    for j in range(3):
        n = int(raw_input())
        l[i].append(n)
        if i == j:
            sum += n

print '-'*10+'matrix'+'-*10'
for i in range(3):
    for j in range(3):
        print l[i][j],
    print

print '-'*10+'matrix'+'-*10'

print 'diagonal summary:',sum

