#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: ex21.py
# Created Time: Fri Apr 22 14:58:49 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

def add(a,b):
    print "ADDing %d + %d"%(a,b)
    return a+b

def subtract(a,b):
    print "SUBStracting %d - %d"%(a,b)
    return a-b

def multiply(a,b):
    print "MULTIPLying %d * %d"%(a,b)
    return a*b

def divide(a,b):
    print "DIVIDING %d / %d"%(a,b)
    return a/b

print "let's do some math with just functions!"

age = add(30,5)
height = subtract(78,4)
weight = multiply(90,2)
iq = divide(100,2)

print "Age: %d,Height: %d,Weight: %d,IQ: %d" % (age,height,weight,iq)

print "Here is a puzzle"

what = add(age,subtract(height,multiply(weight,divide(iq,2))))

print "That becomes: ",what,"Can you do that by hand?"


