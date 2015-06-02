#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: challenge_1.py
# Created Time: Mon Jun  1 22:34:03 2015

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

def convert(msg):
    decode = ""
    for ch in msg:
        if(ch != ' '):
            decode = decode+chr(ord(ch)+2)
        else:
            decode += ' '
    return decode

msg = raw_input("Enter msg\n")

decode = convert(msg)

print decode

