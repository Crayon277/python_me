#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: ex33.py
# Created Time: Sat May  7 21:01:57 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

# while loop

i = 0
number = []
while i<6:
    print "At the top i is %d" % i
    number.append(i)

    i+=1
    print "number now : ",number
    print "At the bottom i is %d"%i

print "the numbers:"
for num in number:
    print num

