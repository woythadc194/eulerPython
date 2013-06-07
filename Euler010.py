"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
from math import ceil
from math import sqrt

SCALE = 2000000

def is_prime(n):
    if n==1:
        return False
    if n==2:
        return True
    for i in range(2, int(ceil(sqrt(n)))+1):
        if n%i==0:
            return False
    return True

total = 0    
for i in range(SCALE):
    if is_prime(i):
        total += i
        
print total
