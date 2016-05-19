#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: 30_digits_reverse_print.py
# Created Time: Thu May 19 14:31:23 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

#给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
from sys import stdout

count=0
def handle(n):
    global count
    if n==0:
        return 
    stdout.write(str(n%10))
    count+=1
    handle(n/10)

number = int(raw_input("> input integer which digits less than 5 "))

handle(number)
print 
print 'digits:',count

