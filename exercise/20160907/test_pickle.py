#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: test_pickle.py
# Created Time: Wed Sep  7 07:04:06 2016

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

import pickle
from print_lol import print_lol

mlist = []

for i in range(20):
    mlist.append(i)

with open('mydata.pickle','wb') as savedata:
    pickle.dump(mlist,savedata)

with open('mydata.pickle','rb') as restoredata:
    l = pickle.load(restoredata)


print locals()
print l
