#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: 8_1_maxfact.py
# Created Time: Sun Sep 11 09:07:33 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

def showMaxFact(num):
    cnt = num/2
    while cnt > 1:
        if num % cnt == 0:
            print num,'has max fact is',cnt
            break
        cnt -= 1
    else:
        print num,'is prime number.'

for i in range(10,21):
    showMaxFact(i)
