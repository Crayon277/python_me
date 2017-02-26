#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: monisen.py
# Created Time: Fri Sep 16 17:25:48 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'


#题目内容：找第n个默尼森数。P是素数且M也是素数，并且满足等式M=2**P-1，则称M为默尼森数。例如，P=5，M=2**P-1=31，5和31都是素数，因此31是默尼森数。

import math
import time
def prime(num):
    for i in range(2,int(math.sqrt(num)+1)):
        if num % i == 0:
            return False
    return True

def monisen(no):
    index = 0
    m_c = []
    p = 2
    while index < no:
        while not prime(p) :
            p+=1
        m = 2**p - 1
        if prime(m):
            m_c.append(m)
            index+=1
        p+=1

    return m_c[-1]

"""
    while 1:
        m = 2**prime_c[no-1]-1
        #prime_c是素数列表
        #这样是有问题的，因为这句话意味着你把第n个monisen数是第n个素数演变过来的，
        #但不是所有的素数按照算法算出来的数都是素数也就是默尼森数，所以还要往后延，
        #这样就不能按照[no-1]这个索引来算了
        if prime(m):
            return m
        else:
            no+=1
"""
start = time.clock()
print 'enter some number'
print monisen(input())
end = time.clock()
print 'time use: %f '%(end-start)
