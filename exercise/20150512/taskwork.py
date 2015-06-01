#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: taskwork.py
# Created Time: Tue May 12 14:34:40 2015

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

import time,sys,Queue
import pdb
from multiprocessing.managers import BaseManager

class QueueManager(BaseManager):
    pass

QueueManager.register('get_task_queue')
QueueManager.register("get_result_queue")

server_addr = '127.0.0.1'

print('Connect to server %s ...'%server_addr)

m = QueueManager(address = (server_addr,5000),authkey = 'abc')

m.connect()

task = m.get_task_queue()
result = m.get_result_queue()
pdb.set_trace()

for i in range(10):
    try:
        n = task.get(timeout = 5)
        
        print ("run task %d * %d"%(n,n))
        r = '%d * %d = %d'%(n,n,n*n)
        time.sleep(1)
        result.put(r)
    except task.empty:
        print("task queue is empty.")

"""
while True:
    try:
        n = task.get()
        if not isinstance(n,int):
            break
        print "task %d * %d"%(n,n)
        r = '%d * %d = %d'%(n,n,n*n)
        time.sleep(1)
        result.put(r)
    except Queue.Empty:
        print ("task queue is empty")
        break
"""        

print ("work exit.")

