#!/usr/bin/env python
# coding=utf-8
'''
itertools.combinations_with_replacement(iterable, r)
This tool returns  length subsequences of elements from the input iterable allowing individual elements to be repeated more than once.

Combinations are emitted in lexicographic sorted order. So, if the input iterable is sorted, the combination tuples will be produced in sorted order.

Sample Code

>>> from itertools import combinations_with_replacement
>>>
>>> print list(combinations_with_replacement('12345',2))
[('1', '1'), ('1', '2'), ('1', '3'), ('1', '4'), ('1', '5'), ('2', '2'), ('2', '3'), ('2', '4'), ('2', '5'), ('3', '3'), ('3', '4'), ('3', '5'), ('4', '4'), ('4', '5'), ('5', '5')]
>>>
>>> A = [1,1,3,3,3]
>>> print list(combinations(A,2))
[(1, 1), (1, 3), (1, 3), (1, 3), (1, 3), (1, 3), (1, 3), (3, 3), (3, 3), (3, 3)]

跟combinations 不一样的是，它允许自己和自己组合，比如，[1,2,3] combinations 是 [(1,2),(1,3),(2,3)] 这个是[(1,1),(1,2),(1,3),(2,2),(2,3),(3,3)], 但（1，2）(2,1)是重复的，

'''


from itertools import combinations_with_replacement
s,k=raw_input().split()
print '\n'.join([''.join(i) for i in combinations_with_replacement(sorted(s),int(k))])
