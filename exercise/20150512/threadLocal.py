#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: threadLocal.py
# Created Time: Tue May 12 11:56:43 2015

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

import threading

local_school = threading.local()

def process_student():
    print "Hello , %s(in %s)"%(local_school.student,threading.current_thread().name)


def run_thread(name):
    local_school.student = name
    process_student()

t1 = threading.Thread(target = run_thread, args = ('Crayon',),name = "1")
t2 = threading.Thread(target = run_thread, args = ("XU",) , name = '7')

t1.start()
t2.start()

t1.join()
t2.join()


