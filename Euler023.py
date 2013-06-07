"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""
import time
from math import sqrt
begin = time.time()

def is_abund(n):
    total = 1                           #start with total==1 and....
    for i in xrange(2, int(sqrt(n)+1)): #range at 2 so we dont add n to total...
        if n%i==0:      
            total += i+n/i              # ...here when n==1
            if n/i==i:
                total -= i
    return total>n  

abundant = []                   #List of abundant numbers
for n in xrange(12,28123+1):    #test every number in range specified by problem
    if is_abund(n):             #if sum_of_divisors > n 
        abundant.append(n)          #append n to abundant

sums = []
for a in abundant:              #test every num in abundant list
    for b in abundant:          #test every num in abundant list
        if a+b < 28123+1:       
            sums.append(a+b)        #add sum of a and b to Sums(of abundant number)
 
print "A:", sum(set(xrange(28123+1)) - set(sums))
print "T:",time.time()-begin    
