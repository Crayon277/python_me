#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: print_lol.py
# Created Time: Wed Sep  7 06:19:56 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'
import sys
def print_lol(mlist,indent=False,level=0,out=sys.stdout):
    for each_line in mlist:
        if isinstance(each_line,list):
            print_lol(each_line,indent,level,out)
        else:
            if indent:
                for tab_stop in range(level):
                    print >>out,'\t'
            print >>out,each_line

