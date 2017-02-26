#!/usr/bin/python
#-*- coding: utf-8 -*-
# File Name: anyIter_test_iter.py
# Created Time: Sat Feb 25 15:57:39 2017

__author__ = 'Crayon Chaney <mmmmmcclxxvii@gmail.com>'

class AnyIter(object):
    def __init__(self,data,safe = False):
        self.__data = data # test. iter(data) 和 就data是不是一样的
        self._safe = safe 
    def __iter__(self):
        return self   # iter(a)的时候返回a，

    def next(self,howmany=1):
        retval = []
        for item in range(howmany):
            #把try放for循环里面，记住，尽量只包含测试语句
            try:
                retval.append(self.data.pop(0))
            except IndexError:
                if self.safe:
                    print "that's all"
                    break
                else:
                    raise
        if len(retval):
            return retval
        else:
            return None
if __name__ == "__main__":
    a = AnyIter(range(10),1)
    for i in range(1,6):
        print a.next(i)

