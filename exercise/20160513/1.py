#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: 1.py
# Created Time: Fri May 13 11:21:10 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

#题目：有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？


candidate = [1,2,3,4]
count = 0
for tri_num in range(123,433):
    winner = tri_num
    single = tri_num % 10
    tri_num /= 10
    tens = tri_num %10
    tri_num /=10
    hundred = tri_num
    
    judge = (single in candidate) and (tens in candidate) and (single != tens and single != hundred and tens != hundred)

    if judge:
        print winner
        count +=1
    
print "all have:",count
    
