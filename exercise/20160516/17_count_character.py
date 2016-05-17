#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: 17_count_character.py
# Created Time: Tue May 17 15:28:08 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

#输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。

toBeCountString = raw_input()

length = len(toBeCountString)

character = 0
space = 0
digit = 0
other = 0

for i in range(length):
    
    if toBeCountString[i].isalpha():
        character +=1
    elif toBeCountString[i].isspace():
        space+=1
    elif toBeCountString[i].isdigit():
        digit+=1
    else:
        other+=1

print 'Original string is: \n%s' %toBeCountString
print 'character count: %d'%character
print 'space count: %d' %space
print 'digit count: %d' %digit
print 'other count: %d' %other
