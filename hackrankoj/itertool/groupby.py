#!/usr/bin/env python
# coding=utf-8

'''
用groupby需要 from itertools import groupby
groupby(list),他返回的是一个迭代 <itertools.groupby object at 0x1026a5a48>

list(groupby(l)) 返回的是
[(iter_first_uniquekey,<itertools._grouper object at 0x1025f50d0>),(iter_second_uniquekey,<itertools._grouper object at 0x1025f50d1>),....]
例如
>>> A＝['1', '2', '2', '2', '3', '1', '1']
>>> list(groupby(A))

[('1', <itertools._grouper object at 0x1026106d0>), ('2', <itertools._grouper object at 0x102610710>), ('3', <itertools._grouper object at 0x102610750>), ('1', <itertools._grouper object at 0x102610790>)]


>>> def gk(l):
...     g=[]
...     k=[]
...     for i,j in groupby(l):
...             g.append(list(j))
...             k.append(i)
...     return g,k
...
>>> groups,key=gk(A)
>>> groups
[['1'], ['2', '2', '2'], ['3'], ['1', '1']]   #在tuple里面的迭代就是原来可迭代对象里面consecutive key group
>>> key
['1', '2', '3', '1']


'''

from __future__ import print_functionx
from itertools import *

for i,j in groupby(map(int,list(raw_input()))):
    print(tuple([len(list(j)), i]) ,end = " ")
