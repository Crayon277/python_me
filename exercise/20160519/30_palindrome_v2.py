#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: 30_palindrome_v2.py
# Created Time: Thu May 19 15:05:12 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

from sys import exit

num = raw_input("> ")

for i in range(len(num)/2): #奇数的话，中间不会进行比较了
    if num[i] != num[-1-i]:
    #利用分片，0要对应-1,1要对应-2
        print '%s is not palindrome'%num
        exit(0)

print '%s is palindrome'%num
