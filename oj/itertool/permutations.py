#!/usr/bin/env python
# coding=utf-8

from itertools import permutations
print '\n'.join([''.join(_) for _ in sorted(list(permutations(*map(lambda s:int(s) if s.isdigit() else s,raw_input().split()))))])
#上面语句的list可以不用写,单纯返回一个迭代器，反正前面有for
'''
permutations(iterable[,k])函数会根据中的iterable的顺序排列，'213'就会先2开头，然后1开头，再3开头，

'''

print '\n'.join([''.join(_) for _ in permutations(*map(lambda s:int(s) if s.isdigit() else sorted(s),raw_input().split()))])
