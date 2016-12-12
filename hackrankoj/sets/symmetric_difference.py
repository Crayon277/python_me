#!/usr/bin/env python
# coding=utf-8


m,l_m,n,l_n = raw_input(),set(raw_input().split()),raw_input(),set(raw_input().split())
print '\n'.join(sorted(l_m^l_n,key=int))

'''
key = int作用是key制定一个function 这里是int,作用在每个元素上，然后按照作用后的元素的值进行cmp。默认直接比

如果这里没有key = int

wrong answer
11
12
5
9

按ascii码，字符[0]的值比较，1在前面。就错了
'''
