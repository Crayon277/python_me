#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: ex39.py
# Created Time: Thu May 12 13:26:28 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

#create a mapping of state to abbreviation
states = {
        'Oregon':'OR',
        'Florida':'FL',
        'California':'CA',
        'New York':"NY",
        'Michigan':'MI'
 }
#create a basic set of states and some cities in them

cities={
        'CA':'San Francisco',
        'MI':'Detroit',
        'FL':'Jacksonville'
}

#add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

#print out some cities
print '-' * 10
print 'NY State has: ', cities['NY']
print 'OR State has: ', cities['OR']

print '-' * 10
print "Michigan's abbreviation is: ",states['Michigan']
print "Florida's abbreviation is: ",states['Florida']

print '-' * 10
print "Michigan has: ",cities[states['Michigan']]
print "Florida has: ",cities[states["Florida"]]

print '-' * 10
for state,abbrev in states.items():
    print "%s is abbreviated %s" %(state,abbrev)

print '-' * 10
for abbrev,city in cities.items():
    print "%s has the city %s"%(abbrev,city)

print '-' * 10
for state,abbrev in states.items():
    print "%s state is abbreviated %s and has city %s"%(state,abbrev,cities[abbrev])

print '-' * 10
state = states.get('Texas',None)

if not state:
    print "Sorry,no Texas."

city = cities.get('TX','Does Not Exist')
print "The city for the state 'TX' is: %s"%city


