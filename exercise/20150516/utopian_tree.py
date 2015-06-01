#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: utopian_tree.py
# Created Time: Sat May 16 16:52:40 2015

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'




T = int(raw_input())
#N = int(raw_input())
def grow(N):
    height = 1
    for i in range(1,N+1):
        if i % 2 == 0:
            height = height + 1
        else :
            height = height * 2
    print height

for i in range(T):
    N = int(raw_input()) 
    grow(N)
    

