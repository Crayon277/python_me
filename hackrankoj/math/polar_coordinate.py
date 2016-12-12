from cmath import polar
polar = polar(complex(raw_input()))
print polar[0]
print polar[1]

#看来polar直接把复数转化为极坐标的形式

'''
我的
from cmath import phase
z=raw_input()
print abs(complex(z))
print phase(complex(z))

abs算出来的表示r，极坐标的长度
phase算出的表示极坐标的角度，弧度制

'''
'''
一开始的难题，怎么提取出1+2j中的1，2。后来发现没必要，但是还是有办法

x,y = map(float,re.findall('[+-]?\d+\.?\d*',raw_input().strip()))

'''

'''
print "\n".join(map(str,(import("cmath").polar(complex(input())))))
还可以这样子！！？？ 貌似编译没有通过
'''
