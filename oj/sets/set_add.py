#!/usr/bin/env python
# coding=utf-8

#我的
n=int(raw_input())
s=set()
for _ in range(n):
    s.add(raw_input())
print len(s)

# V2.
print len(set([raw_input() for _ in range(int(raw_input()))]))

'''
还有一个问题就是，列表解析中的这个raw_input()顺序是怎么样的。
这就要看列表杰西是怎么写的，列表解析可以对应成一个for（嵌套）
上面的可以实质上是
l=[]
for _ in range(int(raw_input())):
    l.append(raw_input())
print len(set(l))

这样就可以看出来先是哪个raw_input了
'''

#v3
print len({raw_input() for x in range(int(raw_input()))})
#s=[] 列表
#s=() 元祖
#s={1,2,3...} 集合(里面是单个元素的)
#s={'1':1,'2':2...} 字典
