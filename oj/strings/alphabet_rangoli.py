#!/usr/bin/env python
# coding=utf-8
"""
#size 3

----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----
"""


"""
#我的思路，先想办法弄出中间的字符,c,cbc,cbabc之类，然后用'-'.join 。问题归结怎么弄出中间的，找规律
from string import lowercase
n = int(raw_input())
for i in range(1,n+1):
    s = lowercase[n-1:n-i:-1]+lowercase[n-i:n] #分左右，中间的归到右边！！很重要。
    print '{:-^{width}}'.format('-'.join(s),width=4*n-3)
for i in range(n-1,0,-1):
    s = lowercase[n-1:n-i:-1]+lowercase[n-i:n]
    print '{:-^{width}}'.format('-'.join(s),width=4*n-3)

"""

import string
alpha = string.ascii_lowercase

n = int(input())
L = []
for i in range(n):
    s = "-".join(alpha[i:n])
    L.append((s[::-1]+s[1:]).center(4*n-3, "-"))
print('\n'.join(L[:0:-1]+L))

#我一直在想 edcbabcde，怎么利用这个对称性，我一直在lowercase做文章，切片。
#其实 上面的思路，abcde，很简单吧，[::-1]就是取反edcba，然后不用去利用lowercase生成新的bcde,直接就可以自身的切片。
# L的原理也是一样。
