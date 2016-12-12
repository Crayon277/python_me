#!/usr/bin/env/python
# coding=utf-8

#这个程序比较用numpy操作数组和纯python操作数组之间的时间上的差异
#这个例子中用的是向量a+向量b，a是0～n的平方，b是0～n的立方
import numpy as np
import sys
from datetime import datetime

def usage_time(func):
    def wrapper(*arg,**kw):
        start = datetime.now()
        result = func(*arg,**kw)
        delta = datetime.now()-start
        return result,delta
    return wrapper

@usage_time
def numpy_add(n):
    a = np.arange(n)**2
    b = np.arange(n)**3
    c = a + b
    return c
@usage_time
def python_add(n):
    a = [x**2 for x in range(n)]
    b = [x**3 for x in range(n)]
    c = [aa+bb for aa,bb in zip(a,b)]
    return c
@usage_time
def python_add_2(n): #这个用的时间比上面的更少一点！！
    a = range(n)
    b = range(n)
    c=[]
    for i in range(len(a)):
        a[i] = i**2
        b[i] = i**3
        c.append(a[i] + b[i])
    return c

size = int(sys.argv[1])
#start = datetime.now()
result,delta = numpy_add(size)
#delta = datetime.now()-start
print 'numpy_add usage time ', delta.microseconds
print 'the last 2 elemnts is ',result[-2:]
#start = datetime.now()
result,delta = python_add(size)
#delta = datetime.now()-start
print 'python_add usage time ', delta.microseconds
print 'the last 2 elements is ',result[-2:]

#start = datetime.now()
result,delta = python_add_2(size)
#delta = datetime.now()-start
print 'python_add_2 usage time ', delta.microseconds
print 'the last 2 elements is ',result[-2:]
