#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: ex38.py
# Created Time: Wed May 11 13:45:20 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there's not 10 things in that list, let's fix that"

stuff = ten_things.split(' ')
more_stuff = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']

while len(stuff)!=10:
    next_one = more_stuff.pop()
    stuff.append(next_one)
    print "add",next_one
    print "now %d items now." %len(stuff)

print "there we go",stuff

new_ten_things = ' '.join(stuff)
print new_ten_things
print '#'.join(stuff[3:5])
print stuff[-1]
