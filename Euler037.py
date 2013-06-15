"""
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""
from time import time
from math import sqrt
start = time()

def is_prime(n):
    if n<=1:
        return False
    if n==2:
        return True
    for i in range(2, int(sqrt(n))+1):
        if n%i==0:
            return False
    return True
    
count = 0
total = 0
n = 11
while count !=11:
    if is_prime(n):
        s = str(n)
        t = s
        right = True
        left = True
        for i in range(1,len(s)):
            s = s[1:]
            if not is_prime(int(s)):
                right = False
        for i in range(1,len(t)):
            t = t[:-1]
            if not is_prime(int(t)):
                left = False
        if right and left:
            total += n
            count += 1
    n += 1
    
print "A:", total
print "T:", time()-start
