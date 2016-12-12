

'''
Task

You are given a space separated list of integers. If all the integers are positive, then you need to check if any integer is a palindromic integer.
palindromic就是回文数

Input Format

The first line contains an integer N. N is the total number of integers in the list.
The second line contains the space separated list of N integers.

Constraints


Output Format

Print True if all the conditions of the problem statement are satisfied. Otherwise, print False.

Sample Input

5
12 9 61 5 14
Sample Output

True
'''

n = input();s = map(int, raw_input().split())
print [False,any(map(lambda x: str(x) == str(x)[::-1], s))][all(map(lambda x: x>0, s))]

'''
用了一个技巧index的方式取值。如果all这里错了，也就是有一个不是positive的，然后[False,*][0] = False
如果all 这里是对的，那再看any

用and比较直观
'''
raw_input()
l=map(int,raw_input().split())
print all(map(lambda x:x>0,l)) and any(map(lambda x:str(x) == str(x)[::-1],l))
#其实如果要处理回文用str的话，输入的时候就不用转化了
