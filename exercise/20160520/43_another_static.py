#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: 43_another_static.py
# Created Time: Fri May 20 10:05:26 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

#模仿静态变量(static)另一案例。

class Num:
    nNum = 1
    def inc(self):
        self.nNum+=1
        print 'nNum = %d'%self.nNum

if __name__ == '__main__':
    nNum = 2
    inst = Num()
    for i in range(3):
        nNum+=1
        print 'The num = %d'%nNum
        inst.inc()


