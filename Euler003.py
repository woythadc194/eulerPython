"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

def prime(x):
    for i in range(2,x/2):
        if x%i==0:
            return False
    if x==1:
        return False
    return True
    
n=600851475143
i=1
while i<n**(1/2):
    if n%i==0 and prime(i):
        print i
    i+=1
