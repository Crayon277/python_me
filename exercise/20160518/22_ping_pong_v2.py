#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: 22_ping_pong_v2.py
# Created Time: Wed May 18 11:30:05 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

#两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。已抽签决定比赛名单。有人向队员打听比赛的名单。a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单。


yi = ['x','y','z']

for a in yi:
    for b in yi:
        if a != b:
            for c in yi:
                judge = (c != a and c != b) and (c == 'y' and a != 'x')
                if judge:
                    print 'a = %c\nb = %c\nc = %c\n'%(a,b,c)
                    
