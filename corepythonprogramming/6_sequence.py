#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: 6_sequence.py
# Created Time: Fri Sep 16 12:51:01 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

#有一个字符串，要求这样显示：每次都把位于最后的一个字符砍掉，显示前面的。
#如：s='abcde'
#abcde
#abcd
#abc
#ab
#a

for i in range(-1,-len(s)):
    print s[:i]

#可是上面第一次迭代的时候没有显示完整的字符串，怎么显示？

for i in [None]+range(-1,-len(s)):
    print s[:i]

# in 后面的就是一个可迭代的对象，‘＋’链接操作符链接后值是[None,-1,-2,-3.....]

#另一个思路，先创建一个只含有None的列表，在用extend方法
for i in [None].extend(range(-1,len(s))):
    print s[:i]
#报错，TypeError
#但是extend函数没有返回值。
#[None].extend()返回None，None既不是序列类型，也不是可迭代的对象。
