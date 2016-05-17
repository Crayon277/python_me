#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: 15_inline_judge.py
# Created Time: Tue May 17 14:44:23 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

#利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。

score = int(raw_input("> "))

if score >= 90:
    print 'A'
elif score >= 60: #进入这个条件的话肯定是小于90的
    print 'B'
else:
    print 'C'

