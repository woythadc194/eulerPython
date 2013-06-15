"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""
from time import time
from math import factorial
start = time()

total = 0
facts = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
n = 2
while n<10000000:
    n+=1
    fact = 0
    for l in str(n):
        fact += facts[(int(l))]
    if n==fact:
        total += n
print "A:",total
print "T:", time()-start
