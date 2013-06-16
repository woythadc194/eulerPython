"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""
from math import sqrt
from itertools import permutations
from time import time
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

n = 9
largest = 0
found = False
while not found:
    temp = list(range(1,n+1))
    pandig = list(permutations(temp))
    for x in reversed(pandig):
        s = ''.join(str(elm) for elm in x)
        if is_prime(int(s)):
            print "A:", s
            found = True
            break
    n -= 1
        
print "T:", time()-start
