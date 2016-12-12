#!/usr/bin/env python
# coding=utf-8

'''
>>> def newfoo(arg1,arg2='default',*vargst,**vargsd):
...     print 'arg1',arg1
...     print 'arg2',arg2
...     for each in vargst:
...             print 'addtional unkown argument',each
...     for each in vargsd.keys():
...             print 'addtional keyword arg %s: %s'%(each,vargsd[each])
...
>>> aTuple = (6,7,8)
>>> aDict = {'z':9}
>>> newfoo(1,2,3,*aTuple,x=4,y=5,**aDict)
arg1 1
arg2 2
addtional unkown argument 3
addtional unkown argument 6
addtional unkown argument 7
addtional unkown argument 8
addtional keyword arg y: 5
addtional keyword arg x: 4
addtional keyword arg z: 9
>>>

可变长参数，用一个元组接收非关键字的事先不知道长度的参数列表
用一个字典接收关键字参数列表

'''
# testit()用其参数地调用了一个给定地函数，成功地话，返回一个和那函数返回值打包地true地返回值，或者False和失败地原因

def testit(func,*nkwargs,**kwargs):
    try:
        retval = func(*nkwargs,**kwargs)
        result = (True,retval)
    except Exception as diag:
        result = (False,diag)
    return result

def test():
    funcs = (int,long,float)
    vals = (1234,12.34,'1234','12.34')

    for eachfunc in funcs:
        for eachval in vals:
            result = testit(eachfunc,eachval)

            if result[0]:
                print 'get right , function %s got %s'%(eachfunc.__name__,result[1])
            else:
                print 'get wrong , function %s got error :%s'%(eachfunc.__name__,result[1])


if __name__ == '__main__':
    test()
