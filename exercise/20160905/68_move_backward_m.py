#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: 68_move_backward_m.py
# Created Time: Mon Sep  5 09:54:10 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

import random
import move_68
# def reverse(mlist):
    # i,j = 0,len(mlist)-1
def reverse(mlist,i,j):
    while i<j:
        mlist[i],mlist[j] = mlist[j],mlist[i]
        i+=1
        j-=1

myList = []
for i in range(10):
    myList.append(random.randint(1,19))

print myList

m = int(input('enter a number:'))


move_68.move(myList,10,m)
print myList


reverse(myList,0,len(myList)-1)
# reverse(myList[0:m-1]) #not working!!
# reverse(myList[m:]) #not working!!
reverse(myList,0,m-1)
reverse(myList,m,len(myList)-1)




print myList
