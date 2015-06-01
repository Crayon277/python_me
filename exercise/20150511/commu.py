#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: commu.py
# Created Time: Mon May 11 18:38:00 2015

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

from multiprocessing import Process , Queue

import os, time ,random

def write(q):
    for value in ['a','b','c']:
        print 'Put %s to queue..'%value
        q.put(value)
        time.sleep(random.random())

def read(q):
    while 1:
        value = q.get(True)
        print "get %s from queue..."%value

if __name__ == "__main__":
    q = Queue()
    pw = Process(target = write, args = (q,))
    pr = Process(target = read,args = (q,))

    pw.start()

    pr.start()

    pw.join()
    pr.terminate()
