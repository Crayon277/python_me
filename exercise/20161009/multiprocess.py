#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: multiprocess.py
# Created Time: Sun Oct  9 22:16:24 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

from multiprocessing import Process
import os 

def run_code(name):
    print 'Run process %s %s'%(name,os.getpid())

if __name__ == '__main__':
    print 'Parent process %s'%os.getpid()
    child = Process(target = run_code,args=('test',))
    print 'Processing start.'
    child.start()
    print 'this is father working %d'%(reduce(lambda x,y:x+y,[i for i in range(100)]))
    child.join()
    print 'Process end.'
