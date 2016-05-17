#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: 18_sum_a_aa_aaa.py
# Created Time: Tue May 17 15:43:01 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

#求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加有键盘控制。

a = int(raw_input("input a > "))
times = int(raw_input("plus times > "))

sum = 0
for i in range(times):
    if i != times-1:
        print '%d + '%a,
    else:
        print '%d'%a,
    sum += a
    a = a*10+a%10
    
print '=',sum
