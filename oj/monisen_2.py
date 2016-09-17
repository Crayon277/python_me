import math
import time
def isprime(num):
    for i in range(2,int(math.sqrt(num)+1)):
        if num % i == 0:
            return False
    return True

def monisen(no):
    p=2
    pnlist=[]
    while len(pnlist)<no:
        if isprime(p):
            pn=2**p-1
            if isprime(pn):
                pnlist.append(pn)
        p+=1
    return pnlist[-1]

start = time.clock()
print monisen(input())
end = time.clock()
print 'time use:%f '%(end - start)
