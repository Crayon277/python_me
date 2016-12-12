#!/usr/bin/python
#-*- coding: utf-8 -*-

# recursive solution
def findall(s, sub):
    if s.find(sub) == -1:
        return 0
    else:
        start = s.find(sub) + 1
        return 1 + findall(s[start:], sub)

string,substring = raw_input(),raw_input()
print findall(string,substring)



#我的方法
# string,substring= raw_input(),raw_input()
#
# cnt = 0
# while 1:
#     try:
#         index = string.index(substring)
#         string = string[index+1:]
#         cnt+=1
#     except ValueError:
#         break
# print cnt


#python3: 利用一个substring长度的滑动窗口对比，这里一个技巧用sum([1 列表解析])，找到一个可能性会在列表中添加一个1，然后加起来就是子串出现的次数
# string, substring = (input().strip(), input().strip())
# print(sum([ 1 for _ in range(len(string)-len(substring)+1) if string[i:i+len(substring)] == substring]))


#python3: 这个对比的方法和上面的大同小异，只是用len方法来算次数，其实没必要，最后这个列表里面肯定都是substring的。
# s1 = input()
# s2 = input()
# print (len([s1[ind:(ind+len(s2))] for ind,x in enumerate(s1) if s1[ind:(ind+len(s2))] == s2]))
