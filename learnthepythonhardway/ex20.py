#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: ex20.py
# Created Time: Fri Apr 22 13:41:22 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

from sys import argv

script, input_file = argv

def print_all(f):
    print f.read()

def rewind(f):
    f.seek(0)

def print_a_line(line_count,f):
    print line_count,f.readline(),

current_file = open(input_file)

print "First let's print the while file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."
rewind(current_file)

print "Let's print three lines:"

for i in range(1,4):
    print_a_line(i,current_file)

print "\n", # 注意，这个是打印两行，一个是\n的，另一个是print函数结束后自己的.如果加一个逗号，那么就只有一个行

print "Now I will show you the line you assigned"
rewind(current_file)
which_line = int(raw_input("> "))

# while (which_line = int(raw_input("> "))) != 0:
    # print "sorry, it has to start from 1"

if which_line <= 0:
    print "what are you kidding me....."
else:
    lines = current_file.readlines()
    count = 0

    for line in lines:
        count+=1
        if count == which_line:
            print line #其实这里也包含着两行，line中有一个\n，print自身\n
        else:
            continue

    if which_line > count:
        print "sorry , your assignment is excess our limit"
