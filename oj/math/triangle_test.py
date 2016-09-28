#!/usr/bin/env python
# coding=utf-8

for i in range(1,int(raw_input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print sum([j*10**(j-1) if j==i else j*10**(j-1)+j*10**(2*i-j-1) for j in range(1,i+1)])
'''
这个思想就是每个要打印的数都给算出来。121=1*10^2+2*10^1+1*10^0 ， 这个思路来。然后找幂的规律

'''
for i in range(1,int(raw_input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print ''.join([str(x) for x in range(1,i)]+[str(x) for x in range(i,0,-1)])

for i in range(1,int(raw_input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print ''.join(map(str,range(1,i)+range(i,0,-1)))
'''
这个的思路就是凑每个打印的东西
'''

#但是题目有限制
# Using anything related to strings will give a score of .
# Using more than one for-statement will give a score of . 第一行已经给出了一个for，也就是不能再用for了

'''
哈哈哈哈
终于被我想出来的！！不能用str的，那就只能算出来，没有import math,也就没有用函数，
那就是需要算出来这个数，最后是一个数，什么函数最后返回的是一个数。

for i in range(1,int(raw_input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print reduce(lambda x,y:x*10+y,range(1,i)+range(i,0,-1))

上面和下面的区别是一个把x当高位，一个把y当高位。

for i in range(1,int(raw_input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print  reduce(lambda x, y: x + (10 ** (y - 1)), range(1, i + 1))**2


'''


'''
其实猜到是应该有关数学的。

The output requires the sequence of Demlo numbers. For n<=9, the squares of the first few repunits are precisely the Demlo numbers. Example: 1^2=1, 11^2=121, 111^2=12321 and so on.
At first lets see how to get repunits. (10^i - 1) / 9 results in the repunits sequence: 1, 11, 111 etc.
Then calculating square of each repunits, we can get Demlo numbers.
So, the code to perform these operations to generate Demlo numbers is:


for i in range(1,int(raw_input())+1):
    print(((10**i)/9)**2)


1*1=1
11*11=121
111*111=12321

以后像这种对称的，可以想象开方，因为对称，一个操作就可以搞定两边，这个解释有点牵强


关于算得。我之前也想过怎么算出来，但我一直纠结i，i只给出1，2，3，4，5 .... 跟121 ， 12321， 跨度有点大，联系不上
找中间商么！！！
'''

'''
还有一种，因为0<n<10

for i in range(0,int(raw_input())):
    print [1, 121, 12321, 1234321, 123454321, 12345654321, 1234567654321, 123456787654321, 12345678987654321, 12345678910987654321][i]

可以偷机
'''



'''
另一个类似的问题。
1
22
333
4444
55555
......

for i in range(1,input()): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print 10**i/9*i

上面更注重数学，

注重编程的：
print sum(map(lambda x: i * 10**x, xrange(i)))
'''
