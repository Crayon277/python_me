#!/usr/bin/env python
# coding=utf-8

#divider,dividend = int(raw_input()),int(raw_input())
#print '\n'.join(map(str,[divider/dividend,divider%dividend,divmod(divider,dividend)]))

#print '\n'.join([str(divmod(int(raw_input()),int(raw_input()))[i]) for i in '01:'])
#这个是错误的，i会是字符，[里面要是int类型的],TypeError: tuple indices must be integers, not str

print '{0}\n{1}\n({0}, {1})'.format(*divmod(int(raw_input()),int(raw_input())))
#我的天哪，这个怎么没有想到呢？？？我一直注重于想把（17，7）怎么分割出来。
