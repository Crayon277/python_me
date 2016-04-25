#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: calc_v1.py

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

import string

operation = "+-*/"

print "Welcome to calclation version 2."
print "Enter your expression  ",
print "(tips:enter 'q','Quit','quit' to exit)"
while True:
    expression = raw_input("> ")
    if string.lower(expression[0]) == 'q':
        break

    if '+' in expression:
        operater = string.split(expression,"+")
        operater1 = int(string.strip(operater[0]))
        operater2 = int(string.strip(operater[1]))
        print "= ",operater1+operater2
    elif '-' in expression:
        operater = string.split(expression,"-")
        operater1 = int(string.strip(operater[0]))
        operater2 = int(string.strip(operater[1]))
        print "= ",operater1-operater2
    elif '*' in expression:
        operater = string.split(expression,"*")
        operater1 = int(string.strip(operater[0]))
        operater2 = int(string.strip(operater[1]))
        print "= ",operater1*operater2
    elif '/' in expression:
        operater = string.split(expression,"/")
        operater1 = int(string.strip(operater[0]))
        operater2 = int(string.strip(operater[1]))
        print "= ",operater1/operater2
    else:
        print "Wrong operation in your expression, please check out!!"

print "Thank you for using calc_v2. See you soon"
