#!/usr/bin/env python
# coding=utf-8

'''
Sample Input

hello world
Sample Output

Hello World

原以为很简单，print ' '.join([s.capitalize() for s in raw_input().split()])
但是就是错在 ' '这里，不一定每个单词之间只有一个空格。

例如hello       world    lol这种。
'''

"""
s=raw_input()
new_s=''
for i in range(len(s)):
    if i == 0 or (s[i-1].isspace() and s[i].isalnum()):
        new_s = new_s + s[i].capitalize()
    else:
        new_s = new_s + s[i]

print new_s
"""


print ' '.join(word.capitalize() for word in raw_input().split(' '))

#这个和我的那个只有一个区别，split(' ')，里面的参数给的是' '，我没有给。
#str.split([sep[, maxsplit]])
#Return a list of the words in the string, using sep as the delimiter string.
#If maxsplit is given, at most maxsplit splits are done
#(thus, the list will have at most maxsplit+1 elements).
#If maxsplit is not specified or -1, then there is no limit on the number of splits (all possible splits are made).
"""
s='hello    world   lol'

s.split()
['hello','world','lol']
============区别=============
s.split(' ')
['hello', '', '', '', 'world', '', '', 'lol']

"""
'''
Title and Capitalise are different in function as:
'abcd'.title()
results in 'Abcd' but
'12abcd'.title()
results in '12Abcd'. This is not what we want.
'''

'''
第三种思路
我只是要改变每个单词的首字母，其它不变。找到，直接改replace
s = input()
for x in s[:].split():
    s = s.replace(x, x.capitalize())
print(s)

'''
