#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: 42_auto_variable.py
# Created Time: Fri May 20 09:18:30 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

#学习使用auto定义变量的用法

#其实就是局部变量

num = 2
def autofunc():
    num = 1
    print 'internal block num = %d'%num
    num += 1

for i in range(3):
    print 'The num = %d'%num
    num += 1
    autofunc()

print 'outside num = %d'%num 
