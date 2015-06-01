#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: loggin.py
# Created Time: Mon May 11 10:23:48 2015

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'
import logging
logging.basicConfig(level = logging.ERROR)
s = '0'

n = int(s)
import pdb

pdb.set_trace()
logging.info("n=%d"%n)

print 10/n
