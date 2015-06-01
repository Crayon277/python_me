#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: thread.py
# Created Time: Tue May 12 08:11:35 2015

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

import time,threading
'''
def loop():
    print "thread %s is running...."%threading.current_thread().name
    n = 0
    while n<5:
        n = n+1
        print 'thread %s >>> %s '%(threading.current_thread().name,n)

        time.sleep(1)
    print "thread %s ended. " %threading.current_thread().name

print "thread %s is running.."%threading.current_thread().name
t = threading.Thread(target = loop)#,name  = "LoopThread")
t.start()
for i in range(5):
    print "%s is running %d"%(threading.current_thread().name,i)
t.join()

print 'Thread %s ended.'%threading.current_thread().name
'''
"""
i,j = 0,1
f = []
def fib(a,b):
    a,b = b, a+b
    return a,b
def run_thread():
    global i,j
    for x in range(100):
        i, j = fib(i,j)
        print "%s produce i = %d  j = %d"%(threading.current_thread().name,i,j)
        f.append(i)
        f.pop()


t = threading.Thread(target = run_thread, name  = "fib_subthread")

tt = threading.Thread(target = run_thread,name = "this_is_other")

t.start()
tt.start()

t.join()
tt.join()
print f

print "Thread %s ended."%threading.current_thread().name

"""

balance = 0

def change(n):
    global balance
    balance +=n
    balance -=n


def run_thread(n):
    for i in range(100000):
        change(n)

t1 = threading.Thread(target = run_thread,name = 'No.1_launch',args = (5,))
t2 = threading.Thread(target = run_thread,name = "NO.2_launch",args= (8,))


t1.start()
t2.start()

t1.join()
t2.join()

print balance

print "%s thread ended."%threading.current_thread().name




