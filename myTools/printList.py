#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: printList.py
# Created Time: Sun Oct  9 22:33:09 2016
'''
This is the standard way to include a 
multiple-line comment in your code.

'''
__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

def pl(listname,indent=0):
    '''
    print nested list.Indent
    '''
    for each_item in listname:
        if isinstance(each_item,list):
            pl(each_item,indent+1)
        else:
            print ' '*indent*4,each_item
