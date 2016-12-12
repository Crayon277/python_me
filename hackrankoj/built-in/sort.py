#!/usr/bin/env python
# coding=utf-8


'''

题目意思就是最后一个先给出5 3 代表5个人，3列，
然后最后的1代表这5行数据按第1列排序，从0开始

Print the  lines of the sorted table. Each line should contain the space separated elements. Check the sample below for clarity.

Sample Input

5 3
10 2 5
7 1 0
9 9 9
1 23 12
6 5 9
1
Sample Output

7 1 0
10 2 5
6 5 9
9 9 9
1 23 12

'''
#我的
nums,lens=map(int,raw_input().split())
l=[]
for _ in range(nums):
    l.append(map(int,raw_input().split()))
k=int(raw_input())
for _ in sorted(l,key=lambda x:x[k]):
    print ' '.join(map(str,_))

#别人的
n,m = map(int,raw_input().split())
lst = []
for i in range(n):
    lst.append(map(int,raw_input().split()))
k = int(raw_input())
print "\n".join(map(lambda x: " ".join(map(str, x)), sorted(lst, key = lambda x: x[k])))
