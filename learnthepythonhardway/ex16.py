#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: ex16.py
# Created Time: Thu Apr 21 20:45:16 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'


from sys import argv

script, filename = argv

file = open(filename,"w+")
print "Input what you want to say"
content = raw_input(">")
file.write(content)

print "here is what you write in %r" % filename
file.seek(0)
print file.read()

file.close()
