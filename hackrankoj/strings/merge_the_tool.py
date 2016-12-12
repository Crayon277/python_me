#!/usr/bin/env python
# coding=utf-8



n,k = raw_input(),int(raw_input())

for i in range(0,len(n),k):
    s=''
    for j in n[i:i+k]:
        if not j in s:
            s+=j
    print s

print '\n'.join([])


"""
S, N = input(), int(input())
for part in zip(*[iter(S)] * N): #什么意思？
    d = dict()
    print(''.join([ d.setdefault(c, c) for c in part if c not in d ]))

"""

'''
l = textwrap.wrap(n,k)

别忘了textwrap这个用法，直接就是把字符串n分成每个长度为k的一个个子串，返回一个列表

>>> s
'AABCAAADA'
>>> textwrap.wrap(s,3)
['AAB', 'CAA', 'ADA']
>>> textwrap.wrap(s,4)
['AABC', 'AAAD', 'A']
>>>

'''

'''
lis=filter(lambda m:m!=lis[0],lis)
filter用法
filter（func,list）,func作用在list上，返回func是true的那些元素组成的list
'''
