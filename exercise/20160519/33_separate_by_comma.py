#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: 33_separate_by_comma.py
# Created Time: Thu May 19 15:53:45 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

#按逗号分隔列表。

l=[1,2,3,4]

sl = ','.join(str(n) for n in l)
print sl
print type(sl)


"""
join(...)
    S.join(iterable) -> string

        Return a string which is the concatenation of the strings in the
        iterable.  The separator between elements is S.

join(里面是一个迭代器！)
"""

