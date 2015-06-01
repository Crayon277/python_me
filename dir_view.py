#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: dir_view.py
# Created Time: Thu May 14 10:59:16 2015

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'
import os
for i in os.walk('.'):
    print i
