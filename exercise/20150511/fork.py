#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: fork.py
# Created Time: Mon May 11 17:48:28 2015

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

import os

# pid = os.fork()

# if pid != 0:
    # print "I am  parent %s and my child is %s"%(os.getpid(),pid)

# else:
    # print "I am child %s"%os.getpid()


from multiprocessing import Process

def run_proc(name):
    print "Run Child process %s(%s)..." %(name,os.getpid())

if __name__ == "__main__":
    print 'Parent Process %s.'%os.getpid()
    p = Process(target = run_proc, args = ("test",))
    print 'Process will start.'

    p.start()
    print 'Among start and begin %s works '%os.getpid()
    p.join()
    print 'Process end.%s'%os.getpid()


