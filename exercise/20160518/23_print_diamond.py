#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: 23_print_diamond.py
# Created Time: Wed May 18 23:02:27 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

'''
   *
  ***
 *****
*******
 *****
  ***
   *
打印菱形
'''
from sys import stdout

for i in range(4):
    stdout.write(' '*(3-i))
    stdout.write('*'*(2*i+1))
    stdout.write('\n')

for i in range(3):
    stdout.write(" "*(i+1))
    stdout.write("*"*(5-2*i))
    stdout.write("\n")
