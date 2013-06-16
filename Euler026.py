"""
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
"""

from decimal import *
from time import time
start = time()

SCALE = 1000

getcontext().prec = SCALE*4

chains = []
chain_length = str(0)
chain_index = 0
n = Decimal(1)
for i in xrange(1, SCALE):
    d = Decimal(i)
    chains.append(str(n/d))
    
for index, chain in enumerate(chains):
    #start at 3 to remove the possibility that the same six digits repeat at the end of the number
    for i in range(3, SCALE): 
        a = chain[-i:]              #working backwards from end of number
        b = chain[-i*2:-i]          #working backwards from start of first chain
        if a==b:                    #once they equal eachother
            if len(a)>len(chain_length):
#                print '1 /',index+1,":",a#,"==",b
                chain_length = a
                chain_index = index
            break

print "A:",chain_index+1," Length:",len(chain_length)#,'('+str(chain_length)+")"
print "T:", time()-start
