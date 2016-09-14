#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: 4_1_typechk.py
# Created Time: Fri Sep  9 15:08:58 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

#this function test if input is a number and what type it is .
#return prompt msg if not


def check(inst):
    print inst,
    if isinstance(inst,(int,float,long,complex)):
        print 'is type of ',type(inst).__name__
    else:
        print 'not number at all'


check(0)
check(9999999999999999999999999999999999999999999999L)
check(0.0)
check(0+0j)
check('dfad')
