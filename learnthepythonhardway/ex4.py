#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: ex4.py
# Created Time: Tue Apr 19 10:21:13 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

car = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = car - drivers
cars_driven = drivers
carpool_capacity = cars_driven*space_in_a_car
average_passengers_per_car = passengers / cars_driven

print "There are",car,"cars available."
print "There are only",drivers,"drivers availabel."
print "There will be",cars_not_driven,"empty cars today."
print "We can transport",carpool_capacity,"people today."
print "We have",passengers,"to carpool today."
print "We need to put about",average_passengers_per_car,"in each car."
print "Is that can be an opition?",average_passengers_per_car < space_in_a_car



