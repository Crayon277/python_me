#!/usr/bin/env python
# coding=utf-8
'''
s,m=map(int,raw_input().split())
print reduce(lambda x,y:x**2+y**2,[max(map(abs,map(int,raw_input().split()[1:]))) for _ in range(s)])%m
#错在reduce上，因为题目中是x1^2+x2^2... 我reduce了之后，前面算好的也会再平方和后面的平方加起来，这样就不对了。
'''
#
# s,m=map(int,raw_input().split())
# print sum([pow(max(map(abs,map(int,raw_input().split()[1:]))),2) for _ in range(s)])%m
'''
还是错了，为什么？题目的要求
You are given a function f(x)= x^2.

You are also given K lists. The i th list consists of Ni elements.

You have to pick exactly one element from each list so that the equation below is maximized:
S=(f(x1)+f(x2)+...+f(xk)) % M

xi denotes the element picked from the i th list . Find the maximized value Smax obtained.

%  denotes the modulo operator.

因为有％m 所以不一定（f＋f＋f...） 最大的就是Smax，因为还要做模运算，形象的理解切掉，你势力太大的，打掉你可能还不如地头蛇了。
'''

from itertools import *
s,m=map(int,raw_input().split())
print max(map(lambda i:sum(i)%m,product(*[map(lambda x:int(x)**2,raw_input().split()[1:]) for _ in range(s)])))



'''
Since this was about itertools, I looked up the documentation and found starmap.
k, m = map(int, raw_input().split(" "))
arrays = [map(int, raw_input().split(" ")[1:]) for _ in xrange(k)]

def f(*nums):
    return sum(x * x for x in nums) % m

print max(itertools.starmap(f, itertools.product(*arrays)))


这里牵扯到一个问题

itertools.imap vs map vs itertools.starmap vs *map

这几个区别是什么

http://www.codenshare.com/2012/04/itertoolsimap-vs-map-vs.html

*map
Notice, however, that this only works when passed as arguments to another function

itertools.starmap vs itertools.imap
The main difference between imap and starmap is that while imap expects a list of items, starmap expects a list of iterables,
which could be a list or a tuple, or anything you can iterate over. So, the list of inputs for imap will look something like [1, 2, 3, 4, 5]
but the list of inputs for starmap will look like [(1,2,3,4,5), (6,7,8,9,10)]:

integers = [(1,2,3,4,5), (6,7,8,9,10)]
print list(itertools.starmap(sum_five, integers))
[15, 40]
The function starmap will call sum_five for each tuple inside the integer list and the result will be
a list of items correspoding to the results of applying sum_five to each tuple in the integers list.

Both imap and starmap do the same thing but they expect the data to to be organized differently.
They provide a convenient way to iterate through the items depending on how your data is structured.


>>> def sum_five(i, j, k, l, m):
...     return i + j + k + l + m
...
>>> list(itertools.imap(sum_five,[(1,2,3,4,5),(5,7,1,2,3)]))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: sum_five() takes exactly 5 arguments (1 given)
>>> list(itertools.imap(sum,[(1,2,3,4,5),(5,7,1,2,3)]))
[15, 18]
>>> list(itertools.starmap(sum_five,[(1,2,3,4,5),(5,7,1,2,3)]))
[15, 18]

上面可以看出，imap 和 starmap 都可以接受[(...),(...),...]这种，反正可迭代的就行，
但是imap把（...）看作一个参数,一个整体，starmap可以把（...）解包传给func

imap()      func, p, q, ...     func(p0, q0), func(p1, q1), ...
imap(pow, (2,3,10), (5,2,3)) --> 32 9 1000
starmap()   func, seq           func(*seq[0]), func(*seq[1]), ...
starmap(pow, [(2,5), (3,2), (10,3)]) --> 32 9 1000

'''
