#!/usr/bin/env python
# coding=utf-8

k=input()
l=raw_input().split()
s=set(l)
for _ in s:
    if l.count(_)!=k:
        print _
    else:
        pass


'''
数学的方法：

k=input()
l=map(int,raw_input().split())
a,s=sum(l),sum(set(l))
print s-(a-s)/(k-1)

算出来这个多余的。题目的意思，给出的K表示，给你的list中的任何一个元素要么出现k次要么1次，找出这个1次的。
(len(l)-1)/k 就是group数。相同数字的表示在同一组（可以看成一个房间，一个房间重复出现的次数就是表示这个房间里面有几个人），
相同数字出现k次，表示这一组里面有k个人，captain是1个人。
sum(l)-sum(s) 其实就是剩下那么多组（组数不变），每组人k-1个人。那么我可以把代表组的编号累加给算出来，然后用sum(s)减掉这个就行了。

类似的想法。只是这里先 k*sum(s) - sum(l) = (k-1)*Captain,然后再除以k-1就行了
The approach to solve this problem follows:
1. Store List: Store the list in a variable. Let roomList be the variable storing the list of room numbers.
2. Room Set: In the variable roomSet, store the set of roomList.
3. Sum Room Set and List: In the variable sumRoomSet and sumRoomList, store the summations of roomSet and roomList, respectively.
4. Multiply K and Subtract: Now, we multiply  with sumRoomSet, subtract the sumRoomList from it and then store the result in the variable temp. Therefore, temp = the Captain's room number  .
5. Divide by K-1: Divide temp by  and store the result in the variable answer.
6. Output: Print answer.
'''

'''
n = int(raw_input());
dic = {}
for x in raw_input().split():
  dic[x] = dic.get(x,0) + 1
for key in dic:
  if dic[key] != n:
    print key
    break

主要学习dict.get()函数
get(...)
    D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.
这里上面的意思，如果x在dic里面，返回dic[x](也就是现在的value)，如果没有返回0，也就是新建一个。
'''
