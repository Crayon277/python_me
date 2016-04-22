#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: ex15.py
# Created Time: Thu Apr 21 21:12:49 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'


from sys import argv

script, filename = argv

txt = open(filename)

print "Here's your file %r: " % filename
print txt.read()

print "Type the filename again: "

file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
