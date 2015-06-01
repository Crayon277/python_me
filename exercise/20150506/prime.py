from math import sqrt
def primes(n):
    if n == 0:
        return []
    elif n == 1:
        return [1]
    else:
        p = primes(int(sqrt(n)))
        no_p = {j for i in p for j in range(i*2, n, i)}
        p = {x for x in range(2, n) if x not in no_p}
    return p

def prime2(n):
        sq = int(sqrt(n))
        notprime = {i for j in range(2,sq) for i in range(j*2,n,j)}
        prime = {i for i in range(n) if i not in notprime}
        return prime
        
print(primes(40))
print
print (prime2(40))
