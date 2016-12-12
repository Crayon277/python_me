#!/usr/bin/env python
# coding=utf-8

'''
You are given a string S.
Your task is to find out whether S is a valid regex or not.

Input Format

The first line contains integer , the number of test cases.
The next  lines contains the string .

Constraints


Output Format

Print "True" or "False" for each test case without quotes.

Sample Input

2
.*\+
.*+
Sample Output

True
False

'''


import re
for _ in range(int(input())):
    ans = True
    try:
        reg = re.compile(input())
    except re.error:
        ans = False
    print(ans)

'''
re.error
https://docs.python.org/2/library/re.html
'''

import re
for _ in range(int(raw_input())):
    try:
        pattern = raw_input()
        re.compile(pattern)
    except:
        print 'False'
    else:
        print 'True'
