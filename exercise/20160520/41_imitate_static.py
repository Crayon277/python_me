#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: 41_imitate_static.py
# Created Time: Fri May 20 08:12:50 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

#模仿静态变量的用法。

def varfunc():
    var = 0
    print 'var = %d'%var
    var +=1



if __name__ == '__main__':
    for i in range(3):
        varfunc()
#if这段只有在此程序作为主程序运行的时候执行，前后面不管怎样都执行

class Static:
    staticVar = 5
    def varfunc(self):
        self.staticVar += 1
        print self.staticVar

print Static.staticVar
a = Static()
for i in range(3):
    a.varfunc()

