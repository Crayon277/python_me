#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: dead_loop.py
# Created Time: Tue May 12 10:41:09 2015

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

import threading,multiprocessing

def loop():
    x = 0
    while True:
        x = x^1


for i in range(multiprocessing.cpu_count()):
    t = threading.Thread(target = loop)
    t.start()


