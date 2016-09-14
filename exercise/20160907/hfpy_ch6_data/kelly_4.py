#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: kelly_4.py
# Created Time: Thu Sep  8 11:10:07 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

#改进：直接继承list就好了

class Athletelist(list):
    def __init__(self,a_name,a_dob=None,a_times=[]):
        list.__init__([])
        self.name = a_name
        self.dob = a_dob
        self.extend(a_times)

    def top3(self):
        return (sorted(set([sanitize(item) for item in self]))[0:3])
#有一个问题，之前我知道列表的名字是self.times,这里是什么？self就是一个列表？？？
#top3 当中的for item in where . where 怎么写？
# !!! 前面的__init__部分，self.extend(a_times) 不是一开始list.__init__(a_times)

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
        return Athletelist(data.pop(0),data.pop(0),data)
    except IOError as err:
        print 'file error' + err


james = get_data('james2.txt')
julie = get_data('julie2.txt')
mikey = get_data('mikey2.txt')
sarah = get_data('sarah2.txt')

print james.name + ' top3 is : '+ str(james.top3())
print julie.name + ' top3 is : '+ str(julie.top3())
print mikey.name + ' top3 is : '+ str(mikey.top3())
print sarah.name + ' top3 is : '+ str(sarah.top3())

print '==adding data===='
james.append('0.12')
print james.name + ' top3 is : '+ str(james.top3())

julie.extend(['2-0','1:45','0.3'])
print julie.name + ' top3 is : '+ str(julie.top3())

