"""
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
"""

from time import time
start = time()

SCALE=1001
n=1                     #starting num
increase = 2
ans = 1                 #starting num

#print n,
while increase<=SCALE-1:
    for i in range(4):
        n += increase
        ans += n
#        print n,
    increase += 2
    
print"A:", ans
print "T:", time()-start
