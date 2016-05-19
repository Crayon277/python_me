#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: 27_reverse_string_by_recursion.py
# Created Time: Thu May 19 10:47:48 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

from sys import stdout

def reverse(s,idx):
    if idx >= len(s):
        return
    reverse(s,idx+1)
    stdout.write(s[idx])

s = raw_input("> ")
reverse(s,0)
print

