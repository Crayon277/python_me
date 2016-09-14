#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: sanitize.py
# Created Time: Wed Sep  7 11:05:59 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'


def sanitize(m):
    if '-' in m:
        splitter = '-'
    elif ':' in m:
        splitter = ':'
    else:
        return m
    (mins,secs) = m.split(splitter)
    return mins+'.'+secs


def sanitize_2(m):
    if m.find('-') == 1:
        m= m.replace('-','.')
    elif m.find(':') == 1:
        m=m.replace(':','.')
    else:
        pass
    return m
