#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: 20_ball_bounce.py
# Created Time: Tue May 17 22:50:45 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

#一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？

distance = 0
bounce = 100.0

for i in range(10):
    if i == 0 :
        distance += bounce
    else:
        distance += bounce*2

    bounce /= 2

print '10th distance: ',distance
print '10th rebound: ',bounce
