#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: delimiter_hyphen.py
# Created Time: Fri Sep 16 21:28:09 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'


print '-'.join(raw_input().split(' '))

#Split and join are useful in many places ... But here I found use of "replace" apt."
print raw_input().replace(' ','-')

#True, but .replace actually creates 2 objects in memory. Split/join perform operations in-place, therefore from a performance point of view you're better off with split()-join()

