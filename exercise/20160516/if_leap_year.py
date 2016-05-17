#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: if_leap_year.py
# Created Time: Tue May 17 15:25:32 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

year = int(raw_input("> "))
print year%4==0 and year %100 !=0 or year % 400 ==0
