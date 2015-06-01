#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: iter.py
# Created Time: Mon May 11 00:29:28 2015

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

class fib(object):
    def __init__(self):
        self.a,self.b = 0,1
    def __iter__(self):
        return self

    def next(self) :
        self.a,self.b = self.b,self.a+self.b
        if self.a > 100:
            raise StopIteration()
        return self.a

    def __getitem__(self,n):
        if isinstance(n,int):
            self.a,self.b = 0,1
            for x in range(n):
                self.a ,self.b = self.b , self.a+self.b
            return self.a
        if isinstance(n,slice):
            start = n.start
            stop = n.stop
            self.a ,self.b = 0,1
            f = []
            for x in range(start):
                self.a, self.b = self.b , self.a + self.b
            for x in range(start,stop):
                self.a,self.b = self.b,self.b+self.a
                f.append(self.a)
            return f
            ###########
             # a,b = 1,1
             # L = []
             # for x in range(stop):
                 # if x >= start:
                     # L.append(a)
                 # a,b = b,a+b
             # return L

for i in fib():
    print i

print 'fib[5] is ',fib()[5]
print 'fib[5:10] is',fib()[5:10]


