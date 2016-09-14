#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: download.py
# Created Time: Sun Sep  4 20:18:34 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

import urllib2

index = 1
def handle():
    for i in range(100):
        file_name = str(index)+'.html'
        base_url = 'http://www.runoob.com/python/python-exercise-example'+str(index)+'.html'
        f=urllib.urlopen(base_url)
        file_download = open(file_name,'w+')
        for line in f.readline():
            file_download.write(line)
        file_download.close()
        index+=1


if __name__ == '__main__':
     # file_name = str(index)+'.html'
     base_url = 'http://www.runoob.com/python/python-exercise-example'+str(index)+'.html'
     f=urllib2.urlopen(base_url)
     # for line in f.readlines():
        #  print line
     line = f.readline()
     print line

