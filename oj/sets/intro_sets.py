#!/usr/bin/env python
# coding=utf-8

raw_input()
s=set(map(int,raw_input().split()))
print(sum(s)/float(len(s)))

'''
reduce(lambda x,y:x+y,list(set(int(x) for x in input().split()))/

利用reduce来计算累加！！！

'''
