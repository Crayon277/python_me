#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: 30_huiwen.py
# Created Time: Thu May 19 14:41:01 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

#一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。

import sys

def digits(n):
    global count
    if n== 0:
        return 
    else:
        digits(n/10)
        count+=1

while 1:
    try:
        num = int(raw_input("> "))
        use_for_print = num
       #解析出是几位数
        count = 0    
        digits(num)
        print count
       #算出中位数的位置position，区分奇偶
        l=[]
        position = count/2
       #position之前入栈，与后面的对比
        for i in range(position):
            l.append(num%10)
            num/=10
        if count & 1 == 1: #说明是奇数位
            num/=10
        flag = 0
        for i in range(position):
            if num%10 != l.pop(): #说明不是回文
                flag = 1
                break
            else:
                num/=10

        if flag:
            print '%d is not palindrome.'%use_for_print
        else:
            print '%d is palindrome!!' %use_for_print
    except EOFError:
        print 'tnx'
        sys.exit(0)


