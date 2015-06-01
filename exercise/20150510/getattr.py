#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: getattr.py
# Created Time: Mon May 11 00:57:33 2015

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

class Chain(object):
    def __init__(self,path = ''):
        self._path = path

    def __getattr__(self,path):
        return Chain('%s/%s'%(self._path,path))

    def __str__(self):
        return self._path


print Chain().status.user.timeline.list
