#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: 4.py
# Created Time: Mon May 16 09:40:13 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

#输入某年某月某日，判断这一天是这一年的第几天？

from sys import exit

def if_primeyear(year):
    return year%4==0 and year%100!=0 or year%400 == 0

mon_days = [31,28,31,30,31,30,31,31,30,31,30,31]

while 1:
    try:
        rawdate = raw_input("> ")
        date = rawdate.split('/')
        year = int(date[0])
        mon = int(date[1])
        day = int(date[2])
        total_day = 0
        for idx in range(1,mon):
            if idx==2 and if_primeyear(year):
                total_day += (mon_days[idx-1]+1)
            else:
                total_day += mon_days[idx-1]

        print '%s is %d day in this year'%(rawdate,total_day+day)
    except EOFError:
        print "thank you"
        exit(0)

