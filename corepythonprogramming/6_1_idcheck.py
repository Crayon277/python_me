#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: 6_1_idcheck.py
# Created Time: Fri Sep 16 16:18:51 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

import string
import sys
begin = string.letters+'_'
houmian = string.letters+string.digits+'_'

test = raw_input()

if test[0] not in begin:
    print 'invalid!!!'
    sys.exit()

for alphabet in test :
    if alphabet not in houmian:
        print 'invalid'
        break
else:
    print 'valid'


