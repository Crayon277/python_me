#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: ex18.py
# Created Time: Fri Apr 22 09:22:43 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

from sys import argv

script = argv

def print_two(*argv):
    arg1,arg2 = argv
    print "arg1:%r,arg2:%r" %(arg1,arg2)

def print_two_again(arg1,arg2):
    print "arg1: %r,arg2: %r" %(arg1,arg2)

def print_one(arg1):
    print "arg1: %r" %arg1

def print_none():
    print "I got nothing."

def checkexist(item):
    file = open(script[0])
    for line in file.readlines():
        if line[:3] == "def" and item in line:
            return "yes"
            break

if __name__ == "__main__":
    checklist = ["print_two","print_two_again","test no","print_one","print_none"]

    for item in checklist:
        print "checking %s..."% item,checkexist(item)

        

    print_two("zed","shaw")
    print_two_again("chenye","xuqiqi")
    print_one("fall in love")
    print_none()

