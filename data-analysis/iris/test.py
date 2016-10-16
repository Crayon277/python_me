#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: test.py
# Created Time: Sat Oct  1 21:40:20 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

fr = open('wr.TRAIN')
fw = open('out.TEST','wb')

content = fr.readline()
content_list = content.split()
print content
print content_list
# for i in content_list[0]:
    # print i.decode('utf-8').encode('utf-8')
fw.write('{0}'.format(content_list).encode())

fr.close()
fw.close()
