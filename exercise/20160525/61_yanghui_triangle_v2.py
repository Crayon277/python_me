#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: 61_yanghui_triangle_v2.py
# Created Time: Wed Jun  1 16:41:43 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

#这个打印杨辉三角的思想就是用二维数组往里面填

if __name__ == "__main__":
    a = []
    for i in range(10):
        a.append([])
        for j in range(10):
            a[i].append(0)

    for i in range(10):
        a[i][0]=1
        a[i][i]=1

    for i in range(2,10):
        for j in range(1,i):
            a[i][j] = a[i-1][j-1]+a[i-1][j]

    from sys import stdout
    for i in range(10):
        for j in range(i+1):
            # stdout.write(str(a[i][j]))
            # stdout.write(' ')
            print '%-3d'%a[i][j],
        print


