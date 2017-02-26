#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: wrap_file.py
# Created Time: Sun Feb 26 10:39:52 2017

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

class CapOpen(object):
    def __init__(self,fn,mode='r',buf=-1):
        self.__file = open(fn,mode,buf)

    def __str__(self):
        return str(self.__file)
    __repr__ = __str__

    def write(self,line):
        self.__file.write(line.upper())

    def __getattr__(self,attr):
        return getattr(self.__file,attr)
    """
    包装还有和派生不一样的地方就是，派生中如果有跟父类重名的就是重载
    包装不是重载，因为假如CapOpen实例化的对象运用点运算符调用了write函数，他是在__dict__中先找有没有write函数
    找不到再去__getattr__中，因为找得到，这个write是成员函数
    但其实这个功能派生也能做到
    """
class CapOpenV2(file):

    def write(self,line):
        super(CapOpenV2,self).write(line.upper())



if __name__ == "__main__":
    """
    f = CapOpen("./tmp.txt",'w')
    print f
    f.write('delegation example\n')
    f.write('faye is good\n')
    f.write('at delegation\n')
    f.close() # 这里是通过__getattr__找到的
    """
    f = CapOpenV2(open('tmp2.txt','w'))
    f.write('delegation example\n')
    f.write('faye is good \n')
    f.close()
