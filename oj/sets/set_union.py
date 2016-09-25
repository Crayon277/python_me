#!/usr/bin/env python
# coding=utf-8

'''
The .union() operator returns the union of a set and the set of elements in an iterable.
Sometimes, the | operator is used in place of .union() operator, but it operates only on the set of elements in set.
Set is immutable to the .union() operation (or | operation).

也就是
>>> s
set([6, 7])
>>> s|[1,2]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for |: 'set' and 'list'
>>> s.union([1,2])
set([1, 2, 6, 7])
>>> s.union({'hello':1,'world':2})
set(['world', 'hello', 6, 7])

用union可以并集一个set和一个可迭代的对象,如list
｜ 操作符只能set 和 set

union一个词典好像只有key会被收编
'''
#我的
n,n_set=input(),set(raw_input().split())
b,b_set=input(),set(raw_input().split())
print len(n_set|b_set)

#one-liner solution
print(len((set(input().split()) if input() != '-1' else '')|(set(input().split()) if input() != '-1' else '')))

#两者区别仅仅在于[],一个有，一个没有［］包起来，这就说明了，if else (else貌似必须要)可以用在任何情况下么？可以起到c语言中的?:操作符作用，只要它有返回值，返回值符合复合语句中的规则
print len(set(*[raw_input().split() if input()!=None else '']) | set(*[raw_input().split() if input()!=None else '']))

#这里相当于把输入的都统一了，反正在这里也用不上。
_,a,_,b=eval("set(input().split()),"*4);print(len(a|b))

#reduce,lambda,[1::2]切片，一系列的技巧。也是把输入都统一了。
print len(reduce(lambda a, b: a | b, [ set(raw_input().strip().split()) for j in range(4)][1::2]))
#reduce返回的是value，这个value根据function来决定，因为这里的lambda和值决定了返回的是一个集合，所以除去len，reduce（）返回的是一个集合
#reduce每次是对［］里面的两个元素应用func，所以这里有［］是没错的

print input() == None or len(set(raw_input().split()).union(input()==None or set(raw_input().split())))
#这个有点意外， 不是输出的真值，也就是真，假（1或0）. 而是输出 先真那一方的值，的值，的值. 所以这里可以利用这一点
'''
>>> print 8*2 or 1-6
16
>>> print 8*0 or 1-6
-5
>>> print 8*2 and 1-6
-5
>>> print 8*0 and 1-6
0

注意和&，｜区别，这两个在下面情况是位运算（取决于两边的数字的类型）！！！还有~,<<,>>,^,会先转成二进制
>>> print 2|6
6
>>> print 1|6
7
>>> print 2 & 6
2
>>> print 1 & 6
0


如果两边是集合，就是集合当中的并，合等操作了

如果两边是一个表达式的话,会先把值算出来,但值类型要，数字和数字，集合和集合。两边都要返回已知的能用&,|操作的数据类型。（或者自定义的类）
>>> print input()==None & sum([x for x in range(4)])
1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for &: 'NoneType' and 'int'
>>> print input()==None or sum([x for x in range(4)])
1
6
>>> print input() & sum([x for x in range(4)])
1
0
>>> print {1,2,3,4} & sum([x for x in range(4)])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for &: 'set' and 'int'
'''
