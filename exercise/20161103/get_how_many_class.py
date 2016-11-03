#!/usr/bin/env python
# coding=utf-8
from collections import OrderedDict
dic=OrderedDict()

with open('TRAIN_3_tags.csv') as fin:
    for item in fin:
        item_list = item.split(',')[1:4]
        item_str = ''.join(item_list)
        dic[item_str] = dic.get(item_str,0)+1
print dic
l=[]
for value in dic.itervalues():
    l.append(value)
l=sorted(l)
print len(l)
print l
if len(l)%2==0:
    print (l[len(l)/2]+l[len(l)/2+1]) / 2
else:
    print l[len(l)/2]

orderdic = sorted(dic,key=lambda x:dic[x])
print orderdic
less_than_10=[]
for key,value in dic.iteritems():
    if value < 6 :
        less_than_10.append(key)
print less_than_10
