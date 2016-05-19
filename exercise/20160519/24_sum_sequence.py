#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: 24_sum_sequence.py
# Created Time: Thu May 19 09:28:15 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

#有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。

dividend = 2.0
divisor = 1.0
sum = 0

for i in range(20):
    sum += dividend/divisor
    dividend = dividend + divisor
    divisor = dividend - divisor

print sum


