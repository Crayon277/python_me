#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: ex9.py
# Created Time: Tue Apr 19 16:42:51 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print "Here are the days:",days
print "Here are the months: ",months

print "here is raw format of printing month %r" % months 
#that's how formatting works, \n newlines not work when i use %r

print """
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
"""
