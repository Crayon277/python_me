#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: 67_v2.py
# Created Time: Mon Sep  5 09:33:41 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

import random

def inp(mList):
    for i in range(10):
        mList.append(random.randint(1,10))
    print mList

def max_min(mList):
    imax = imin = 0
    for i in range(10):
        if mList[i]>mList[imax]:
            imax = i
        else:
            pass
        if mList[i]<mList[imin]:
            imin = i
        else:
            pass
    mList[0],mList[imax] = mList[imax],mList[0]
    mList[9],mList[imin] = mList[imin],mList[9]

def oup(mList):
    print mList

if __name__ == '__main__':
    myList = []
    inp(myList)
    max_min(myList)
    oup(myList)

