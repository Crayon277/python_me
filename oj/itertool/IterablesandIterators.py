#!/usr/bin/env python
# coding=utf-8



'''
The itertools module standardizes a core set of fast, memory efficient tools that are useful by themselves or in combination.
Together, they form an iterator algebra making it possible to construct specialized tools succinctly and efficiently in pure Python.

To read more about the functions in this module, check out their documentation here.
You are given a list of  lowercase English letters. For a given integer ,
you can select any  indices (assume -based indexing) with a uniform probability from the list.

Find the probability that at least one of the  indices selected will contain the letter: ''.

Input Format

The input consists of three lines. The first line contains the integer , denoting the length of the list.
The next line consists of  space-separated lowercase English letters, denoting the elements of the list.

The third and the last line of input contains the integer , denoting the number of indices to be selected.

Output Format

Output a single line consisting of the probability that at least one of the  indices selected contains the letter:''.

Note: The answer must be correct up to 3 decimal places.

Sample Input

4
a a c d
2
Sample Output

0.8333
Explanation

All possible unordered tuples of length  comprising of indices from  to  are:


Out of these  combinations,  of them contain either index  or index  which are the indices that contain the letter ''.
(1,2),(1,3),(1,4),(2,3),(2,4),(3,4)
Hence, the answer is 5/6.

其实完全没必要用index，直接用输入的。
'''


from itertools import combinations
length = int(raw_input())
print '%f'%(sum([1 if 'a' in str(item) else 0 for item in combinations(raw_input().split(),int(raw_input()))])/float(sum(range(length))))

'''
上面的代码有两个问题，第一个问题就是因为我算那个长度，是sum(range(length))，因为按照例子给出的，2个selected，的时候就是1+2+3，不加4，数学问题中的组合的个数，
但这只是局限于两个两个组合的情况！！！
另外一个问题就是，当长度为1的时候，range(1) = 0,他会除以0
float(sum(range(length)) or 1) 这是一种解决方法，但是没有解决第一个问题
'''


from itertools import combinations
length = int(raw_input())
s,k=raw_input().split(),int(raw_input())
print '%f'%(sum([1 if 'a' in str(item) else 0 for item in combinations(s,k)])/float(reduce(lambda x,y:x*y,range(length,length-k,-1))/reduce(lambda x,y:x*y,range(k,0,-1))))

'''
中学学的C(m,n) = n*(n-1)*...*(n-m+1)/m*(m-1)*..*1 这就是组合数
'''


'''
用filter解法

from itertools import combinations

N = int(input())
L = input().split()
K = int(input())

C = list(combinations(L, K))
F = filter(lambda c: 'a' in c, C)
print("{0:.3}".format(len(list(F))/len(C)))
'''


'''
一个牛人的，纯数学解题

Sorry, but the problem has nothing to do with using itertools. This is a pure probability exersize. Just replace your last three lines with:
M = ''.join(L).count('a')
print 1.0 - reduce(lambda x,y: x*y,[(1.0-M*1.0/(N-i)) for i in xrange(K)])

We have a sequence of N charatcters. M of them are 'a'. We perform K selections of random elements from the sequence.
The goal is to calculate the probability of at least one character in the selected K elements is 'a'.
Lets calculate the probability p of an event where none of the selected elements is 'a'.
#他这里为什么反面算，因为at least one ， 至少有一个就行了，正面的话要把aa,ab,ac,ab,ac的情况都算一遍。
If K=1, then the probability of selecting anything but 'a' is p = 1-M/N. If K=2, we are seleting two elements.
The probability of none of the two being 'a' is the probability of the first element is not 'a': (1-M/N) times the probablity of the second element is not 'a': (1-M/(N-1)).
 The denominator is N-1 because the lenght of the secuence is N-1 after taking out the first element while the number of 'a's remains same.
p = (1-M/N) * (1-M/(N-1))
If K=3 then
p = (1-M/N) * (1-M/(N-1)) * (1-M/(N-2))
and so on.
That is how we calculate the probability p of no 'a's selected out of K tries. The problem statement of this challenge is to calculate the probability of at least one 'a' seleted.
Then the result is
1 - p

也就是我们现在所要算的
4
a a c d
2

'a'出现了两次，因为我们是要选择2个球。
他把所有可能结果中有含有a球的组合占多少比例，转化成算我抽两个球，抽到a的概率是多少。这两个等价么？
'''
