"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""
import time
begin = time.time()

def sum_of_divisors(n):
    total = 0
    for i in range(1, n):
        if n%i==0:
            total += i
    if n==1:
        total = 1
    return total

total_sum = 0

abundant = []                   #List of abundant numbers
for n in range(28123):          #test every number in range specified by problem
    x = sum_of_divisors(n)      
    if x>n:                     #if sum_of_divisors > n 
        abundant.append(n)          #append n to abundant
    target = True               #bool for if n is a sum of two abundant numbers
    for a in abundant:          #test every num in abundant list
        b = n-a
        if b in abundant:       #if n-abundant_num == another_abundant_num
            target = False          #number is not target (we want n!=abund+abund)
            break                   #we already know number isnt target so break
    if target:
        total_sum += n
            
print "A:",total_sum
print "T:",time.time()-begin    

