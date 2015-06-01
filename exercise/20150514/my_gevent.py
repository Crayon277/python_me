#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: my_gevent.py
# Created Time: Thu May 14 21:48:36 2015

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

from gevent import monkey; monkey.patch_socket()

import gevent

def f(n):
    for i in range(n):
        print gevent.getcurrent(),i
        gevent.sleep()

g1 = gevent.spawn(f,5000)
g2 = gevent.spawn(f,5000)
g3 = gevent.spawn(f,5000)
g1.join()
g2.join()
g3.join()


