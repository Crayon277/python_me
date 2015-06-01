#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: taskmanager.py
# Created Time: Tue May 12 14:21:01 2015

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

import random,time,Queue

from multiprocessing.managers import BaseManager

task_queue  = Queue.Queue()

result_queue = Queue.Queue()

class QueueManager(BaseManager):
    pass

QueueManager.register('get_task_queue',callable = lambda:task_queue)
QueueManager.register("get_result_queue",callable = lambda:result_queue)

manager = QueueManager(address = ('',5000),authkey = 'abc')
manager.start()

task = manager.get_task_queue()
result = manager.get_result_queue()

while True:
    try:
        n = int(raw_input("> "))
        print('put task %s..'%n)
        task.put(n)
    except EOFError:
        break
print("try get results...")

while True:
    try:
        r = result.get()
        print ("result : %s"%r)
    except result.empty:
        print "All result have been received"
        break


manager.shutdown()


