#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: 67_handle_list.py
# Created Time: Mon Sep  5 09:03:35 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

import random

myList=[]

for i in range(10):
    myList.append(random.randint(1,10))

print myList

my_sort_list=myList
my_sort_list.sort()
max_n = my_sort_list[9]
min_n = my_sort_list[0]

max_index = myList.index(max_n,0,len(myList))

print 'max_index is',max_index

myList[0],myList[max_index]=myList[max_index],myList[0]
print myList
#因为交换之后，要重新算那个min_index，有可能会发生改变，有可能第一个元素就是最小的
min_index = myList.index(min_n,0,len(myList))
print 'min_index is',min_index
myList[9],myList[min_index]=myList[min_index],myList[9]

print myList

