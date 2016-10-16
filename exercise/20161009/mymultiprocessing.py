#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: multiprocessing.py
# Created Time: Sun Oct  9 22:10:20 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

import os

print 'Process %s start ...'%os.getpid()

child = os.fork()

if child == 0 :
    print 'I am child process %s and my parent is %s.'%(os.getpid(),os.getppid())
else:
    print 'I am father %s , my child is just born %s.'%(os.getpid(),child)
