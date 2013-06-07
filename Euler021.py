"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a  b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""
from math import ceil
from math import sqrt
def amicable(n):
    x = sum_of_divisors(n)
    if n == sum_of_divisors(x):
        return x
    return False
    
def sum_of_divisors(n):
    total = 0
    for i in range(1, n):
        if n%i==0:
            total += i
    if n==1:
        total = 1
    return total
    
total = 0
for i in range(10000): 
    return_val = amicable(i)
    if type(return_val)==int:
        if i!=return_val:
            print i,':',return_val
            total += i
print total
