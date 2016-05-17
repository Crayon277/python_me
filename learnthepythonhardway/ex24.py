#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: ex24.py
# Created Time: Thu Apr 28 19:14:53 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

print 'you\'d need to know\'bout escapes with \\ taht do \n newlines and \t tabs.'

poem = """
\tThe lovely world 
with logic so firmly planted
cannot disern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""


print "----------------"
print poem
print "----------------"

five = 10 - 2 + 3 -6
print "This should be five : %s" % five

def secret_formula(started):
    jelly_beans = started*500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans,jars,crates

start_point = 10000
beans, jars, crates = secret_formula(start_point)

print "With a starting point of : %d" % start_point
print "We'd have %d beans , %d jars, and %d crates." %(beans,jars,crates)

start_point = start_point / 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates."%secret_formula(start_point)


