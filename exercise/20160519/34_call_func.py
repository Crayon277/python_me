#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: 34_call_func.py
# Created Time: Thu May 19 16:01:19 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

#练习函数调用。

def hello_world():
    print "hello world"

def three_greet():
    for i in range(3):
        hello_world()

if __name__ == '__main__':
    three_greet()
