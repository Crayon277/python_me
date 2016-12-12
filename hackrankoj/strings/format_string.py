#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: format_string.py
# Created Time: Fri Sep 16 21:40:50 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

print "hello %s %s! welcome to python world"%(raw_input(),raw_input())

print 'Hello {0} {1}! welcome to python world'.format(raw_input(),raw_input())

print 'hello',raw_input(),raw_input(),'! welcome to python world'
print 'hello'+' '+raw_input()+' '+raw_input()+'! welcome to python world'

#In this case, there is no difference. "+" does actual string concatenation, 
#and "," is a way to tell the print statement to end the printout with a blank space instead of a new line.
