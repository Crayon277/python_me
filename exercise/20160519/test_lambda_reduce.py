#!/usr/bin/env python
#-*- coding: utf-8 -*-

import time

def test_factorial_reduce():
    '''
    Function:使用reduce函数
    Input：NONE
    Output: NONE
    author: socrates
    blog:http://blog.csdn.net/dyx1024
    date:2012-02-19
    '''     
    time_begin = time.clock()
    print reduce(lambda x,y:x*y, range(1, long(raw_input("please input a number ( > 0):"))))
    print "Use time: %s" % (time.clock() - time_begin)
       
    return;

def test_factorial_math():
    '''
    Function:使用math库函数
    Input：NONE
    Output: NONE
    author: socrates
    blog:http://blog.csdn.net/dyx1024
    date:2012-02-19
    '''     
    import math
    time_begin = time.clock()
    print math.factorial(long(raw_input("please input a number ( > 0):")))
    print "Use time: %s" % (time.clock() - time_begin) 
    
if __name__ == '__main__':
    
    print '*' * 50 + "Use reduce" + '*' * 50
    test_factorial_reduce()
    
    print '*' * 50 + "Use math api" + '*' * 50
    test_factorial_math()




