#!/usr/bin/python
#-*- coding: utf-8 -*-

'''
Perform append, pop, popleft and appendleft methods on an empty deque .

Sample Input

6
append 1
append 2
append 3
appendleft 4
pop
popleft


Sample Output

1 2
'''


from collections import deque
d=deque()
for _ in range(int(raw_input())):
    exec('d.{}({})'.format(*(raw_input().split()+[''])))
print ' '.join(map(str,d))


'''
getattr
'''

from collections import deque
d = deque()
for _ in range(int(input())):
    inp = input().split()
    getattr(d, inp[0])(*[inp[1]] if len(inp) > 1 else [])
print(*[item for item in d])
