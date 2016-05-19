#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: 31_which_week.py
# Created Time: Thu May 19 15:11:43 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

#请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。

# import string

# weekname = raw_input("> ")

# if string.capitalize(weekname[0]) == 'M':
    # print 1
# elif string.capitalize(weekname[0]) == 'W':
    # print 3
# elif string.capitalize(weekname[0]) == 'F':
    # print 5
# elif string.capitalize(weekname[0]) == 'T':
    # if string.capitalize(weekname[3]) == 'E':
        # print 2
    # else:
        # print 4
# else:
    # if string.capitalize(weekname[1]) == 'A':
        # print 6
    # else:
        # print 7

letter = raw_input('> ')
if letter.lower() == 's':
    letter = raw_input("> input second letter ")
    if letter.lower() == 'a':
        print 'Saturday'
    elif letter.lower() == 'u':
        print 'Sunday'
    else:
        print 'Error'
elif letter.lower() == 'm':
    print 'Monday'
elif letter.lower() == 'w':
    print 'Wednesday'
elif letter.lower() == 'f':
    print 'Friday'
elif letter.lower() == 't':
    letter = raw_input("> input second letter ")
    if letter.lower() == 'u':
        print 'Tuesday'
    elif letter.lower() == 'h':
        print 'Thursday'
    else:
        print 'Error'
else:
    print 'Error'
