#!/usr/bin/python
#print math.sin(12) 
import math
import os
n = int(math.sqrt(100))
noprime = [j for i in range(2,n) for j in range(i*2,100,i)]
prime = [i for i in range(100) if i not in noprime ]
print prime
