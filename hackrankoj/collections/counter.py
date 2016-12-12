#!/usr/bin/python
#-*- coding: utf-8 -*-


from collections import Counter
raw_input()
shoes = Counter(raw_input().split())
earn = 0
for _ in range(int(raw_input())):
    i,j=raw_input().split()
    if shoes[i]>0:
        earn += int(j)
        shoes[i]-=1
print earn

'''
奇怪我上面的这个为什么会通过？
因为假如i不在shoes里面会报错啊！
'''
