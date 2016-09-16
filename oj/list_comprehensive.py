#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: list_comprehensive.py
# Created Time: Fri Sep 16 07:15:18 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

x = input()
y = input()
z = input()
n = input()

final = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n]
print final


#===== v2

x,y,z,n = input(),input(),input(),input()

#print 下面一样

#-====== v3
x,y,z,n = (input() for _ in range(4))

#相当于 (x,y,z,n) = (input(),input(),input(),input()) 右边外面的()不要忘了！！！
