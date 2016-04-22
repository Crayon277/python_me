#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: ex17.py
# Created Time: Thu Apr 21 22:03:47 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" %(from_file,to_file)

in_file = open(from_file)
indata = in_file.read()
#indata = open(from_file).read()

print "The input file is %d bytes long " % len(indata)

print "Does the output file exist? %r " % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file,'w')
out_file.write(indata)

out_file.close()
in_file.close()
raw_input()

