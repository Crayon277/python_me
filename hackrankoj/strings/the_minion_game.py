#!/usr/bin/env python
# coding=utf-8

"""
vowels = 'AEIOU'
s_input = raw_input()
stuart=0
kevin = 0
sub_list = []
def check_freq(sub,s):
#    return sum([1 for i in range(len(s)+1-len(sub)) if s[i:i+len(sub)] == sub])
#    上面这个其实是有问题！！因为 range(len(s)+1-len(sub)) 意思，假如sub是‘AN’ len(s)+1-len(sub)是5,这个
#    5的意思是我可以比较5个，BANANA,BA,AN,NA,NA,NA,但是这个单个查找总共出现几次sub的情况下。在这里，还要考虑的是
#    是否重复，因为我外面还有一层大循环。就拿AN来说，我这次的AN是BANANA，B后的第一个AN，检查到有两个，累加上。但是
#    后面还有一次AN,那会再累加上2次，就这算多余了。而且sub是A这种一个字符的情况下，后面算自身都是多余的，因为第一个A
#    就会计算出总共有几个A。
# '''
#     if not sub in sub_list:
#         sub_list.append(sub)
# 这里不能放在sum()的前面，因为里面有一句比较 not s[] in sub_list, 提前加进去了，所有都在了，就不会算子串了。
#
#     return sum([1 for i in range(len(s)+1-len(sub)) if not s[i:i+len(sub)] in sub_list and s[i:i+len(sub)] == sub])
# '''
    if sub in sub_list:
        return 0
    else:
        sub_num = sum([1 for i in range(len(s)+1-len(sub)) if not s[i:i+len(sub)] in sub_list and s[i:i+len(sub)]==sub])
        sub_list.append(sub)
        return sub_num

def check(special,s):
    freq = 0
    for length in range(1,len(s)+1-special):  #每次从这个开头步进一个长度形成子串，再去检测这个子串的出现次数
        freq+=check_freq(s[special:special+length],s)
    return freq
for i in range(len(s_input)):  #循环每一个字符当作子串的开头。
    if s_input[i] in vowels:
        kevin += check(i,s_input)
    else:
        stuart += check(i,s_input)
if stuart > kevin:
    print 'Stuart',stuart
elif stuart < kevin:
    print 'Kevin',kevin
else:
    print 'Draw'


这种方法在检测字符串超级长的时候效率非常低！！！
"""

"""
#改变思路，先把所有子串都弄出来，然后一个一个来检查有几个，第一个字母是元音辅音决定加到stuart还是kevin上
myString = raw_input()
ms_len = len(myString)
# sub_list = list(set([ for length in range(1,len(myString)+1)]))
sub_list = []
for i in range(1,ms_len+1):
    for j in range(ms_len+1-i):
        if not myString[j:j+i] in sub_list:
            sub_list.append(myString[j:j+i])
        #print sub_list
#能不能一句话实现上面的？
# sub_list = list(set(sub_list))
# print sub_list
vowels = 'AEIOU'
kevin,stuart = 0,0
def freq(sub):
    return sum([1 for i in range(ms_len+1-len(sub)) if myString[i:i+len(sub)] == sub])

for sub in sub_list:
    if sub[0] in vowels:
        kevin += freq(sub)
        print 'k',kevin
    else:
        stuart += freq(sub)
        print 's',stuart

if stuart > kevin:
    print 'Stuart',stuart
elif stuart < kevin:
    print 'Kevin',kevin
else:
    print 'Draw'

对input04.txt数据量很大的时候，这个算法还是不行，但是比第一种方法要好。
"""

#===================================
'''
Hmm, I kept timing out, until I figured out that this doesn't actually require
any string processing other than recognizing vowels. It's pure mathematics.

# 解法。我的思路在看到题目中的子串的出现次数记分的规则就被局限住了，我联想到之前算子串的sum（[1 ]）的方法
# 就想着怎么找到子串，然后去运用这个方法来算子串的出现次数。其实这里面有三个循环，第一个开头，第二个以这个开头来形成各个长度的子串
# 第三，再遍历字符串与各个长度的子串比较算出子串的出现次数。这个复杂性很高！！！

什么是算法，什么是数学，什么是结合？
其实这里上面的算法是可以解，但是时间耗费太长太长，要优化算法。一种优化是语法上，函数调用之类的。一种是算法上，就是整体的思路
BANANA, 我们可以知道他所有的子串，但真的有必要都列出来吗？因为，B带头的都是stuart的，B带头的有6种可能性
然后是A带头的，都是kevin的，有5种可能性，以此类推。但是怎么算这个子串的次数？我的思维就是局限于算出每个子串，然后每个子串再去算次数
而且考虑到重复次数，还要再排除。

其实总的子串个数是确定的。length*(length+1)/2，也就是6+5+4+3+2+1（以BANANA为例），这就是所有的子串的个数，想一下，也就是
stuart ＋ kevin 的分数的总和！很重要！这个思路的转变提供了新的方向。不用比较子串，也不用考虑重复，因为总要算上去，
就想while 里面有比较，是一次性比较完，还是用while来执行这个比较（意会）。

还是已BANANA为例，B开头的子串个数是6，就是字符串的长度。因为B是辅音，所以这些都算在stuart上，那么这些子串要算出现的次数么？
不用，因为我们相当于是遍历所有的子串，那些重复的后面会算到，但是这个遍历所有的子串并不是将所有的子串都列出来，因为没有必要列出来
以这个字符开头的子串的个数就是这个字符到最后这个字符串的长度。

首先积分的规则是辅音开头的子串出现次数算stuart，因为重复是因为后面的字符串有相同，但是我们到后面会以那个字符开头算。

This challenge can be solved by finding all the substrings of the string and separating the substrings on the basis of their first character.

If the string is BANANA, the substrings are:
B
BA
BAN
BANA
BANAN
BANANA

A
AN
ANA
ANAN
ANANA

N
NA
NAN
NANA

A
AN
ANA

N
NA

A

It is interesting to note that in BANANA:
Words formed using the first letter B       = 6
Words formed using the second letter A  = 5
Words formed using the third letter N     = 4
Words formed using the fourth letter A    = 3
Words formed using the fifth letter N      = 2
Words formed using the last letter A       = 1
Using this pattern, you can run a loop from the start to the end of the string and filter out words starting with vowels and consonants.

'''

"""
#Crazy 4-liner in Python 3, it only needs 0.15 for case 14. :D
w = input().strip()
kscore = sum(map(lambda i, c: i if (c in "AEIOU") else 0, range(len(w), 0, -1), w))

#map的这个函数很赞！！！其实和下面的思路是一样的，但是简化了一步

sscore = len(w) * (len(w) + 1) // 2 - kscore
print("Draw" if kscore == sscore else "Kevin {}".format(kscore) if kscore > sscore else "Stuart {}".format(sscore))
"""




'''
The logic is simple - take all possible substrings, split them into two sets

according to starting letter, then sum elements in sets.

All possible substrings are string of lenght 1, then strings of length 2 etc.

i above is an iterator for that lenght.

And then comes a little optimization - if you know the starting letter,

you can add all substrings of different length that start with this letter. It will be len(s) - i
'''
s = raw_input()

vowels = 'AEIOU'

kevsc = 0
stusc = 0
for i in range(len(s)):
    if s[i] in vowels:
        kevsc += (len(s)-i)
    else:
        stusc += (len(s)-i)

if kevsc > stusc:
    print "Kevin", kevsc
elif kevsc < stusc:
    print "Stuart", stusc
else:
    print "Draw"



#优化，range()->xrange() won't store the whole list in memory

#优化，len(S) 事先算出来。 可是我有一个疑问。为什么range(len(s))会每次算len(s).
#     range()产生一个列表，然后for 每次迭代。每次算的话？都去取第一个值？

#写法优化  print 'Stuart ' + str(stuart) if stuart > kevin else 'Kevin ' + str(kevin)

"""
minion = str(input())
minion = minion[::-1]
#把这里反过来的意义在于后面vow+=(i+1) 看上去更简单一点，但是原理还是和上面的一样
vowels = ['A','E','I','O','U']
cons = 0
vow = 0
for i in range(len(minion)):
    if minion[i].upper() in vowels:
        vow += (i+1)
    else:
        cons += (i+1)

"""



'''
#上面算出一个元音的再算另一个辅音的可以再简化。
#总数是确定的，减掉就可以了。

string = raw_input().strip()
totalScore = len(string)*(len(string)+1)/2
scoreKevin = 0
vowels = ['A', 'E', 'I', 'O', 'U']
for i in range(len(string)):
    if string[i] in vowels:
        scoreKevin += len(string)-i
if scoreKevin>(totalScore-scoreKevin):
    print 'Kevin', scoreKevin
elif scoreKevin == (totalScore-scoreKevin):
    print 'Draw'
else:
    print 'Stuart', (totalScore-scoreKevin)

# 语法特性，sum算kscore
import string
s = input()
l = len(s)

Total = sum([l- i for i in range(l)])
Kscore = sum([l-i if s[i] in 'AEIOU' else 0 for i in range(l)])


#enumerate

for i, a in enumerate(string):
    if a in "AEIOU":
        kevin_score += string_len - i
    else:
        stuart_score += string_len - i

'''
