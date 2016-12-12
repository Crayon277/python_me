#!/usr/bin/env python
# coding=utf-8

#这个程序要做的是随机选择+，- 运算符号，然后随机选择两个运算数，显示出来，让你计算，然后有两次机会是否计算正确

from operator import add,sub
from random import choice#,randint

oper = {'+':add,'-':sub}
def dropr():
    #s随机选择 运算符号
    op=choice('+-')
    #随机选择两个运算数
    nums = [choice(range(10)) for n in range(2)]
    #nums = [randint(1,10) for n in range(2)]
    ans = oper[op](*nums)
    print '{0} {1} {2} ='.format(nums[0],op,nums[1])
    chances = 0
    maxtries=2
    #while chances < 2: #这里的2是最大尝试次数，不能硬编码！！
    while chances < maxtries
        get_ans = int(raw_input())
        if get_ans == ans:
            print 'you are right'
            break
        elif get_ans != ans:
            print 'oops , try again'
            chances+=1
    else:
        print 'your chances run out'

def main():
    while True:
        dropr()
        try:
            if_continue = raw_input('continue ? [y/n]')
            if if_continue == 'n':
                break
        except (KeyboardInterrupt,EOFError):
            break

if __name__ == '__main__':
    main()
