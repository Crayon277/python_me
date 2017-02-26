#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: wrap_me.py
# Created Time: Sun Feb 26 09:26:50 2017

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

class WrapMe(object):
    def __init__(self,obj):
        self.__data = obj

    def __str__(self):
        return str(self.__data)
    
    def __repr__(self):
        return 'self.__data'
    def get(self):
        return self.__data
    def __getattr__(self,attr):
        return getattr(self.__data,attr)
    def __getitem__(self,index):
        return self.__data[index]
