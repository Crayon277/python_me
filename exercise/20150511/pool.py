#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: pool.py
# Created Time: Mon May 11 18:18:57 2015

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

from multiprocessing import Pool
import os,time,random

def long_time_task(name):
    print "run task %s (%s)"%(name,os.getpid())
    start = time.time()
    time.sleep(random.random()*3)
    end = time.time()
    print "Task %s runs %0.2f seconds." %(name,(end - start))

if __name__ == "__main__":
    print "parent process %s."%os.getpid()
    p = Pool()
    for i in range(9):
        p.apply_async(long_time_task,args = (i,))
    print "Waiting for all subprocess done..."
    p.close()
    
    print "See if child can run this code? or Parent %s "%os.getpid()

    p.join()
    print "all subprocess done"

