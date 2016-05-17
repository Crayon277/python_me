#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: 13_shuixianhua.py
# Created Time: Mon May 16 22:54:47 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

#打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。

def if_true(num):
    cube_sum = 0
    tmp = num
    while num!=0:
        cube_sum += (num%10)**3
        num /= 10
    if tmp == cube_sum:
        return True
    else:
        return False

for i in range(101,1000):
    if if_true(i):
        print i
