#!/usr/bin/env python
# coding=utf-8



from collections import deque
d=deque()
for _ in range(int(raw_input())):
    a,flag=0,0
    lens,value=raw_input(),map(int,raw_input().split())
    d.extend(value)
    while len(d) !=0 :
        if flag and max(d[-1],d[0]) > a:
            print 'No'
            break
        if d[-1] > d[0]:
            a=d.pop()
        else:
            a=d.popleft()
        flag=1
    else:
        print 'Yes'
