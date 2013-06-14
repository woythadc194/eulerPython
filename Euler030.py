"""
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""
import time
start = time.time()

EXP = 5

def sum_of_pow(n, exp):
    x = 0
    for l in str(n):
        x += int(l)**exp
    return x

total = 0
for n in range (2,1000000):
    if n==sum_of_pow(n,EXP):
        total += n

print "A:", total
print "T:", time.time()-start
