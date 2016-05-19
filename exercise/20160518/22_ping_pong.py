#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: 22_ping_pong.py
# Created Time: Wed May 18 10:06:36 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

#两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。已抽签决定比赛名单。有人向队员打听比赛的名单。a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单。


yi = ['x','y','z']

for a in yi: #这里为什么a只执行了一次循环！！！
    tmp = yi #因为python里的赋值不是重新建立一个存储单元，而是在相同的存储单元（真正的数值上）再贴一个标签，两者操作的是相同的实体
    tmp.remove(a) #本来是设想另起一个tmp用来当做b的循环
    print a    
    print tmp
    for b in tmp:
        tmpc = tmp
        tmpc.remove(b)
        print tmpc
        c = tmpc[0]
        if a!='x' and c == 'y':
            print 'a = %s\nb = %s\nc = %s\n'%(a,b,c)
        

        


