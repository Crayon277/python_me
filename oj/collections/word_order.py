#!/usr/bin/python
#-*- coding: utf-8 -*-

'''
Task
You are given  words. Some words may repeat. For each word, output its number of occurrences.
The output order should correspond with the input order of appearance of the word. See the sample input/output for clarification.

Sample Input

4
bcdef
abcdefg
bcde
bcdef
Sample Output

3
2 1 1

'''

from collections import OrderedDict
od = OrderedDict()
for _ in range(int(raw_input())):
    item = raw_input().strip()
    od[item]=od.get(item,0)+1
print len(od)
print ' '.join([str(value) for value in od.itervalues()])


'''
牛人用继承！！
'''

from collections import Counter, OrderedDict
class OrderedCounter(Counter, OrderedDict):
    pass
d = OrderedCounter(input() for _ in range(int(input())))
print(len(d))
print(*d.values())
