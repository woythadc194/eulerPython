"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

from math import sqrt
from math import ceil

SCALE = 10001

def is_prime(n):
    if n==1:
        return False
    if n==2:
        return True
    for i in range(2, int(ceil(sqrt(n)))+1):
        if n%i==0:
            return False
    return True
    
count = 0
x = 0
while count != SCALE:
    x += 1
    if is_prime(x):
        count += 1
        
print x
