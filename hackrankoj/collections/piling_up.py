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

'''s
上面有一个重大的bug，就是test case 和test case 之间 d=deque() 的d没有清洗，上一个测试例还有残留项

'''

'''
brilliant solution!!!!
'''

for t in range(input()):
    input()
    lst = map(int, raw_input().split())
    l = len(lst)
    i = 0
    while i < l - 1 and lst[i] >= lst[i+1]:
        i += 1
    while i < l - 1 and lst[i] <= lst[i+1]:
        i += 1
    print "Yes" if i == l - 1 else "No"

'''
其实这个task主要就是从一个队列中取前后最大的，堆起来（金字塔型，下面最大，往上依次递减），堆不起来主要原因就是我在堆的时候发现这个比前一个大，
这样反映在队列中的形式就是，两边肯定最大，依次往中间收缩，

可以画一个趋势图，现递减，然后递增
'''
