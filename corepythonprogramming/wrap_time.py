#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: wrap_time.py
# Created Time: Sun Feb 26 18:48:52 2017

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

from time import time,ctime

class TimedWrapMe(object):
    def __init__(self,obj):
        self.__data = obj
        self.__ctime = self.__atime = self.__mtime = time()

    def get(self):
        self.__atime = time()
        return self.__data

    def gettimeval(self,t_type):
        if not isinstance(t_type,str) or t_type[0] not in 'cma':
            raise TypeError,"argument of 'c','m',or'a' req'd"
        return getattr(self,'_%s__%stime'%(self.__class__.__name__,t_type[0]))
    """
    这个getattr 返回的是self._TimedWrapMe__c/m/atime
    为gettimestr做铺垫。。还以为什么用
    """
    def gettimestr(self,t_type):
        # return ctime(eval('self._%s__%stime'%(self.__class__.__name__,t_type[0])))
        return ctime(self.gettimeval(t_type))

    def set(self,obj):
        self.__atime = self.__mtime = time()
        self.__data = obj

    # def __repr__(self):
        # self.__atime = time()
        # return self.__data

    def __str__(self):
        self.__atime = time()
        return str(self.__data)
    __repr__ = __str__

    def __getattr__(self,attr):
        self.__atime = time()
        return getattr(self.__data,attr)

