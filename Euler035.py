"""
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""
from time import time
from math import sqrt
start = time()

primes = []

def is_prime(n):
    if n<=1:
        return False
    if n==2:
        return True
    for i in range(2, int(sqrt(n))+1):
        if n%i==0:
            return False
    return True

for i in range(1000000):
    s = str(i)
    if is_prime(i):
        circular = True
        for j in range(len(s)):
            s = s[1:] + s[0]
            if not is_prime(int(s)):
                circular = False
                break
        if circular:
            primes.append(str(i))
            
print "A:", len(primes)
print "T:", time()-start
