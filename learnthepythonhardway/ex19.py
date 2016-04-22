#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: ex19.py
# Created Time: Fri Apr 22 11:22:53 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'


from sys import argv

script = argv

def myfun(argv1,argv2):
    return "argv1 is %r\nargv2 is %r" %(argv1,argv2)

def value(init = 10):
    return init+1

op = 1

print op
print myfun(1,2)
op+=1
print op
print myfun(op,2);
op+=1
print op
print myfun(op+2,op+3)

op+=1
print op
print myfun(value(),value())

op+=1
print op
print myfun(value(),1)

op+=1
print op
print myfun(value(op),value(12))

op+=1
print op
print myfun(script[0],script)
op+=1

print op
print myfun(open("test.txt").read(),2)
op+=1

print op
print myfun(int(raw_input("> ")),raw_input("> "))
op+=1
