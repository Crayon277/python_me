#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: mkdir.py
# Created Time: Fri May 13 11:09:20 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

import time
import os
from sys import exit

dir_name = "%d%02d%02d"%(time.localtime().tm_year,time.localtime().tm_mon,time.localtime().tm_mday)

if os.path.exists(dir_name):
    print "%s already exist!"%dir_name
    exit(0)
else:
    os.mkdir(dir_name)

