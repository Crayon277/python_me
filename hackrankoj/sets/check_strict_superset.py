#!/usr/bin/env python
# coding=utf-8

A=set(raw_input().split())
print all([A>set(raw_input().split()) for _ in range(input())])

'''
all(iter) iter中要全部都是true才返回true，有一个false就返回false。
这里检查A是不是所有集合的严格超集，都是True才是，所以用all
'''
