#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: ex14.py
# Created Time: Thu Apr 21 00:00:14 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

from sys import argv

script, user_name = argv
prompt  = '> '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt+"yes/no ")

if likes[0] == "y":
    print "so glad to hear that"
else:
    print "sorry to hear that,i will come back better."

print  "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print "who is your love?"
love = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
I'm sure %r will regret leaving you. 
"""%(likes,lives,computer,love)
