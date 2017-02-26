#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: 13_9_descr.py
# Created Time: Sun Feb 26 22:34:47 2017

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

"""
这个类是一个雏形，但他展示了描述符的一个有趣的应用，可以在一个文件系统上保存属性的内容
"""

import os
import pickle

class FileDescr(object):
    saved = []

    def __init__(self,name = None):
        self.__name__ = name

    def __get__(self,obj,type=None):
        if self.name not in FileDescr.saved:
            raise AttributeError,"%r used before assignment"%self.name
    
    try:
        f = open(self.name,'r')
        val = pickle.load(f)
        f.close()
        return val
    except(pickle.UnpicklingError,IOError,EOFError,AttributeError,ImportError,IndexError),e:
        raise AttributeError,"could not read %r: %s"%self.name

    def __set__(self,obj,val):
        f = open(self.name,'w')
        try:
            try:
                pickle.dump(val,f)
                FileDescr.saved.append(self.name)
        except(TypeError,pickle.PicklingError),e:
            raise AttributeError,"could not pickle %r"%self.name
        finally:
            f.close()

    def __delete__(self,obj):
        try:
            os.unlink(self.name)
            FileDescr.saved.remove(self.name)
        except(OSError,valueError),e:
            pass


