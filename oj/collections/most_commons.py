#!/usr/bin/env python
# coding=utf-8


'''
You are given a string S.
The string contains only lowercase English alphabet characters.

Your task is to find the top three most common characters in the string S.


Sample Input

aabbbccde

Sample Output

b 3
a 2
c 2

'''


#my solution
from collections import Counter
print '\n'.join([' '.join(map(str,l)) for l in sorted(sorted(Counter(raw_input()).most_common(3)),key=lambda x:x[1],reverse=True)])


#other colution

S = raw_input()
letters = [0]*26

for letter in S:
    letters[ord(letter)-ord('a')] += 1

for _ in range(3):

    max_letter = max(letters)

    for index in range(26):
        if max_letter == letters[index]:
            print chr(ord('a')+index), max_letter
            letters[index] = -1
            break
#Counter Solution 1

from collections import Counter
from operator import itemgetter

for item in (sorted(sorted(Counter(raw_input()).items()), key = itemgetter(1), reverse = True)[:3]):
    print item[0], item[1]

#Counter Solution 2

from collections import Counter

for letter, counts in sorted(Counter(raw_input()).most_common(),key = lambda x:(-x[1],x[0]))[:3]:
    print letter, counts

'''
key = lambda x:(-x[1],x[0])
现对-x[1]排，在对x[0]排

'''
# solution 2
from collections import Counter, OrderedDict

class OrderedCounter(Counter, OrderedDict):
    pass
[print(*c) for c in OrderedCounter(sorted(input())).most_common(3)]



'''
OrderedCounter

OrderedCounter
 |  Method resolution order:
 |      OrderedCounter
 |      collections.Counter
 |      collections.OrderedDict
 |      __builtin__.dict
 |      __builtin__.object

计算读入的相同字符，然后根据插入的顺序排。 可以先对输入的字符串排序

https://codefisher.org/catch/blog/2015/06/16/how-create-ordered-counter-class-python/

'''
