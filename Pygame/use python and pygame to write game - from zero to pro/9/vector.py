#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: vector.py
# Created Time: Thu Feb 23 07:50:03 2017

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'
import math
class Vector2(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return "(%s,%s)"%(self.x,self.y)

    @classmethod
    def from_points(cls,P1,P2):
        return cls(P2[0]-P1[0],P2[1]-P1[1])
    
    def get_magnitude(self):
        return math.sqrt(self.x**2+self.y**2)

    def normalize(self):
        magnitude = self.get_magnitude()
        return Vector2(self.x/magnitude,self.y/magnitude)
        #return self.__class__(self.x/magnitude,self.y/magnitude)


A = (10.0,20.0)
B = (30.0,35.0)
AB = Vector2.from_points(B,A)

print AB
print AB.normalize()
