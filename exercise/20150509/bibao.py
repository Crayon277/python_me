#!/usr/bin/python

# New Concept. Named Bi Bao in chinese.
# See the example

def sum(x):
    f = []
    for i in x :
        def fn(j):
            def gn():
                return j*j
            return gn
        f.append(fn(i))
    return f

x,y,z = sum([1,2,3])
print x()
print y()
print z()
