#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: kelly_2.py
# Created Time: Wed Sep  7 22:27:47 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'


def sanitize(l):
    if '-' in l:
        splitter = '-'
    elif ':' in l:
        splitter = ':'
    else:
        return l
    mins,secs = l.split(splitter)
    return mins+'.'+secs

def get_data(filename):
    try:
        with open(filename) as f:
            data = f.readline().strip().split(',')
        return {
                'name':data.pop(0),
                'dob':data.pop(0),
                'top3': str(sorted(set([sanitize(item) for item in data]))[0:3])
                }
    except IOError as err:
        print 'file error' + err
james = get_data('james2.txt')
julie = get_data('julie2.txt')
mikey = get_data('mikey2.txt')
sarah = get_data('sarah2.txt')

print james['name'] + 'top3 is :' + james['top3']
print julie['name'] + 'top3 is :' + julie['top3']
print mikey['name'] + 'top3 is :' + mikey['top3']
print sarah['name'] + 'top3 is :' + sarah['top3']
