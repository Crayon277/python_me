#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: thread_im.py
# Created Time: Tue May 12 10:36:03 2015

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

import time,threading

balance = 0
Lock = threading.Lock()
def change(n):
    global balance
    balance += n
    balance -= n

def run_threan(n):
    for i in range(100000):
        Lock.acquire()
        try:
            change(n)
        finally:
            Lock.release()

t1 = threading.Thread(target = run_threan, name = "1" , args = (5,))
t2 = threading.Thread(target = run_threan, name = '2' ,args = (8,))

t1.start()
t2.start()

t1.join()
t2.join()

print balance

print "%s end"%threading.current_thread().name
    
