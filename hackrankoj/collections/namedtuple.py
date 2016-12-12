#!/usr/bin/python
#-*- coding: utf-8 -*-
'''
namedtuple

Code 01

>>> from collections import namedtuple
>>> Point = namedtuple('Point','x,y')
>>> pt1 = Point(1,2)
>>> pt2 = Point(3,4)
>>> dot_product = ( pt1.x * pt2.x ) +( pt1.y * pt2.y )
>>> print dot_product
11

就是给一个tuple 比如（1，2）赋予实际的意义，然后建立一个类，每一个元素对应一个属性，这里建立的是Point类，两个元素分别对应x,y
然后tuple中访问元素时就可以不用t[0]这种integer indices, 而像类属性那样的访问名字t.x就可以了

Code 02

>>> from collections import namedtuple
>>> Car = namedtuple('Car','Price Mileage Colour Class')
>>> xyz = Car(Price = 100000, Mileage = 30, Colour = 'Cyan', Class = 'Y')
>>> print xyz
Car(Price=100000, Mileage=30, Colour='Cyan', Class='Y')
>>> print xyz.Class
Y

这里主要说明了
classname = namedtuple(typename, field_names, verbose=False, rename=False)
1、field_names 的给值可以由字符串空格隔开的形式给出，也可以字符串逗号形式，统一csv格式。也可以list等迭代的
2、建立namedtuple的时候使用classname建立，不是typename
当打印一个namedtuple类的时候显示typename。
'''


'''
Task

Dr. John Wesley has a spreadsheet containing a list of student's IDs,Marks , Name and Class.

Your task is to help Dr. Wesley calculate the average marks of the students.


TESTCASE 01

5
ID         MARKS      NAME       CLASS
1          97         Raymond    7
2          50         Steven     4
3          91         Adrian     9
4          72         Stewart    5
5          80         Peter      6
TESTCASE 02

5
MARKS      CLASS      NAME       ID
92         2          Calum      1
82         5          Scott      2
94         2          Jason      3
55         8          Glenn      4
82         2          Fergus     5
Sample Output

TESTCASE 01

78.00
TESTCASE 02

81.00

输入的时候
MARKS的位置不一定！！！这对于不用这个方法是一个难点。

'''


from collections import namedtuple
all = int(raw_input())
student = namedtuple('student',raw_input())
score = 0
for _ in range(all):
    s=student(*(raw_input().split()))
    score+=int(s.MARKS)
print score/float(all)


'''

'''

from collections import namedtuple
N = int(input());student = namedtuple('student',input().strip().split())
print(sum(float(student(*input().strip().split()).MARKS) for _ in range(N))/N)
