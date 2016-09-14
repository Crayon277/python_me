#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: kelly_3.py
# Created Time: Thu Sep  8 10:06:26 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'


class Athlete:
    def __init__(self,a_name,a_dob=None,a_times=[]):
        self.name = a_name
        self.dob = a_dob
        self.times = a_times

    def top3(self):
        return (sorted(set([sanitize(item) for item in self.times]))[0:3])
#调用者来决定写一步做什么，而不是在top3就定死要做什么，这里可以直接在top3里用print 打印出
#其他信息，也可以转换为字符串，但那样太不灵活了。
#考虑扩展，不要定死
    def add_time(self,value):
        self.times.append(value)
    
    def add_times(self,value_list):
        self.times.extend(value_list)


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
        return Athlete(data.pop(0),data.pop(0),data)
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
james.add_time('0.12')
print james.name + ' top3 is : '+ str(james.top3())

julie.add_times(['2-0','1:45','0.3'])
print julie.name + ' top3 is : '+ str(julie.top3())


#从上面功能来看，Athlete类的功能其实就是list功能，两个的区别仅仅只是多了两个属性
