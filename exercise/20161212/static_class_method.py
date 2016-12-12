#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: static_class_method.py
# Created Time: Mon Dec 12 21:33:14 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

class Foo:
    x= 1
    y = 2
    @staticmethod
    def average(*args):
        return sum(args)/float(len(args))

    @staticmethod
    def static_method():
        return Foo.average(Foo.x,Foo.y)

    @classmethod
    def class_method(cls):
        return cls.average(cls.x,cls.y)

class Son(Foo):
    x = 3
    y = 5

    @staticmethod
    def average(*args):
        '''
        重载父类的average函数
        '''
        return sum(args)/float(3)


p = Son()
print p.static_method()
print p.class_method()
print Son.static_method()
print Son.class_method()
print Foo.static_method()
print Foo.class_method()
