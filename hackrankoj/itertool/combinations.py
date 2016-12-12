#!/usr/bin/env python
# coding=utf-8


'''
itertools.combinations(iterable, r)  注意r这个参数一定要给，跟permutations是不一样的

>>> from itertools import combinations
>>>
>>> print list(combinations('12345',2))
[('1', '2'), ('1', '3'), ('1', '4'), ('1', '5'), ('2', '3'), ('2', '4'), ('2', '5'), ('3', '4'), ('3', '5'), ('4', '5')]
>>>
>>> A = [1,1,3,3,3]
>>> print list(combinations(A,4))
[(1, 1, 3, 3), (1, 1, 3, 3), (1, 1, 3, 3), (1, 3, 3, 3), (1, 3, 3, 3)]

组合也就是不重复，(1,2) (2,1)算一样的， 但是例子中给出的1，1，3，3，3，虽然元素一样，但是可以这样理解是随着位置，index来组合

'''

from itertools import combinations
s,k = raw_input().split()
for _ in reduce(lambda x,y:x+y,[list(combinations(sorted(s),i)) for i in range(1,int(k)+1)]):
    print ''.join(_)



'''
>>> data = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
>>> new = [y for x in data for y in x]
>>> new
[0, 1, 2, 3, 4, 5, 6, 7, 8]
涉及到怎样把［［］，［］］内嵌的给剥离开只有一个［］
我用了reduce, 一开始用*编译 报错
'''

'''
另外一个问题，交换了次序会怎样？
>>> data = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
>>> [y for x in data for y in x]
[0, 1, 2, 3, 4, 5, 6, 7, 8]
>>> [y for y in x for x in data]
[6, 6, 6, 7, 7, 7, 8, 8, 8]

这里之所以出现这种情况只是因为x是上一个遗留的
如果先来下面那个会报错

>>> data = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
>>> [y for y in x for x in data]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'x' is not defined

为什么三个6，三个7，三个8

>>> for y in x:
...     for x in data:
...             print x,y
...
[0, 1, 2] 6
[3, 4, 5] 6
[6, 7, 8] 6
[0, 1, 2] 7
[3, 4, 5] 7
[6, 7, 8] 7
[0, 1, 2] 8
[3, 4, 5] 8
[6, 7, 8] 8

因为内嵌的for 会执行3次
'''
