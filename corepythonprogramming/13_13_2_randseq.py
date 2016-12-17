#!/usr/bin/env python
# coding=utf-8

from random import choice

class RandSeq(object):
    def __init__(self,seq):
        self.data = seq

    def __iter__(self):
        return self #仅返回self,这就是如何讲一个对象声明为迭代器的方式

    def next(self):
        return choice(self.data)
        #没有终点，无穷迭代

if __name__ == '__main__':
    rs = RandSeq([1,2,3,4])
    for i in rs:
        print i
