#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: test.py
# Created Time: Wed Mar  1 18:38:53 2017

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

import re
import os
import shutil
import sys

path_a = sys.argv[1]
path_b = sys.argv[2]

file_list_a = os.listdir(path_a)
file_list_b = os.listdir(path_b)

p = re.compile('\w+')

for file_name in file_list_b:
    to_be_copy = p.match(file_name).group()
    for item in file_list_a:
        file_path = path_a+'/'+item
        if to_be_copy in item and os.path.isfile(file_path):
            shutil.copy(file_path,path_b)
            print 'move %s to %s'%(item,path_b)

