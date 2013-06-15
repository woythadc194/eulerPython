"""
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
"""
from time import time
start = time()

def reduced(n,d):
    for x in range(2,n+1):
        if n%x==0 and d%x==0:
            return reduced(n/x,d/x)
    print n,'/',d
    return

masterN = 1
masterD = 1
for n in range(10,100):
    for d in range(n+1,100):       
        n1 = float(str(n)[0])
        n2 = float(str(n)[1])
        d1 = float(str(d)[0])
        d2 = float(str(d)[1])
        a = float(n)/float(d)

        if(n1==d1 and d2!=0 and a==n2/d2)or(n2==d1 and d2!=0 and a==n1/d2)or(n1==d2 and a==n2/d1)or(n2==d2 and a==n1/d1 and n2!=0):
            masterN *= n
            masterD *= d
            print n,'/',d
        
print "A:",
reduced(masterN,masterD)
print"T:",time()-start
