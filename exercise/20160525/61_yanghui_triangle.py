#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: 61_yanghui_triangle.py
# Created Time: Wed May 25 15:08:40 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

#打印出杨辉三角形 10行

format = 9


print ' '*format,
format-=1
print 1

print ' '*format,
format-=1
print '1 1'

l = [1,1]
for i in range(8):
    print ' '*format,
    # print 'format is :',format
    format-=1
    print 1,
    new_l = []
    for i in range(len(l)-1):
       new_l.append(l[i]+l[i+1])
    # print 'new_l is ',new_l
    for i in range(len(new_l)):
        print new_l[i],
    new_l.insert(0,1)
    new_l.insert(len(new_l),1)
#上面两步一定要加打印两边的是独立的，但没有为下一次考虑，不然下一次就计算错误。
    l = new_l

    print 1
    
