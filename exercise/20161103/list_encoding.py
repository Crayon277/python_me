#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: list_encoding.py
# Created Time: Fri Oct  7 17:25:08 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'


def list_encode(l,enc='utf-8'):
    new_l = []
    for i in l:
        new_l.append(i.encode(enc))
    return new_l
