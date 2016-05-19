#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: 29_ask_age.py
# Created Time: Thu May 19 14:17:41 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

#有5个人坐在一起，问第五个人多少岁？他说比第4个人大2岁。问第4个人岁数，他说比第3个人大2岁。问第三个人，又说比第2人大两岁。问第2个人，说比第一个人大两岁。最后问第一个人，他说是10岁。请问第五个人多大？



def final_age(n):
    if n == 1:
        return 10
    else:
        return final_age(n-1)+2

print final_age(5)
#这么想，n就是代表第几个人，因为n=1的时候return 10就是第一个人10岁
#第n个人是 final_age(n-1)+2 岁，现在要算第五个, n就传5就行了
