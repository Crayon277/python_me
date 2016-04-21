#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: ex6.py
# Created Time: Tue Apr 19 15:48:13 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Thos who know %s and those who %s."%(binary,do_not)

print x
print y
print "I said: %s." %x
print "I also said: '%s'." % y
hilarious = False
joke_evaluation = "Isn't  that joke so funny! %r"
print joke_evaluation % hilarious
w = "This is the left side of ..."
e = "a string with a right side."

print w + e

