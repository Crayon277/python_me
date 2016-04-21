#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: ex8.py
# Created Time: Tue Apr 19 16:13:45 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

formatter = "%r %r %r %r"

print formatter % (1,2,3,4)
print formatter % ("one","two","three","four")
print formatter % (formatter,formatter,formatter,formatter)
print formatter % ( # don't forget the comma that split every single meta data
        "I had this thing.",
        "That you could type up right.",
        "But it didn't sing.",
        "So I said goodnight."
        )
print formatter % (
        "你好",
        "谢谢",
        "我爱你",
        "再见"
        )
print "%s %s %s %s" % ( # have to set the format to %s to print chinese, or it will be weird symbols
        "你好",
        "谢谢",
        "我爱你",
        "再见"
        )
