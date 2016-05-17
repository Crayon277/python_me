#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: 2_2.py
# Created Time: Fri May 13 15:05:28 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

from sys import exit

arr = [1000000,600000,400000,200000,100000,0]
rat = [0.01,0.015,0.03,0.05,0.075,0.1]

while 1:
    try:
        benefit = int(raw_input("> "))
    except EOFError:
        print "Out"
        exit(0)

    bonus = 0
    for i in range(0,6):
        if benefit > arr[i]:
            bonus += (benefit-arr[i])*rat[i]
            benefit = arr[i]

    print bonus
