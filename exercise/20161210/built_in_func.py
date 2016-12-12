#!/usr/bin/env python
# coding=utf-8

#filter函数，比如你在一个果园摘了一些果子，出去的时候如果能进过一个自动把不好的果子丢掉的一个装置的就好了
#filter调用一个函数，然后对一个可迭代的对象中的元素执行这个函数，最终留下这个函数返回值是True的元素
#如果函数是None的话，那么返回元素为true的列表
#用纯python 代码实现这个功能

def myfilter(bool_func,seq):
    if bool_func:
        return [x for x in seq if bool_func(x)]
    else:
        return [x for x in seq if x]
def test_filter():
    test_seq = [1,-1,1,1,1,-1,-1,-1,0,1]
    print myfilter(lambda x:x>0,test_seq)
    print myfilter(None,test_seq)

#map函数，用纯 python实现，是将seq每个元素有执行一遍func
#如何用纯python实现map的多参数那个功能？？？？？
def mymap(func,seq):
    return [func(x) for x in seq]

def test_map():
    test_seq = [1,2,3,4]
    print mymap(lambda x:x*2,test_seq)

def myreduce(func,seq,init=None):
    seq = list(seq) #确定这是list对象
    if init is None:
        res = seq.pop(0) #从一开始的迭代中，我们拿了两个元素，因为我们没有从先前的值中获得一个结果。
    else:
        res = init  #如果这个没有那要init干嘛
    for each in seq:
        res = func(res,each)
    return res

def test_reduce():
    test_seq = [1,2,3,4,5]
    print myreduce(lambda x,y:x+y,test_seq)
if __name__ == '__main__':
    # test_map()
    test_reduce()
