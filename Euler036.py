"""
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""
from time import time
start = time()

def is_pal(s):
    t = ""
    for l in s:
        t = l + t
    return s==t
    
total = 0
for n in range(1000000):
    if is_pal(str(n)):
        if is_pal(bin(n)[2:]):
#            print n, '=', bin(n)[2:]
            total += n
            
print "A:", total
print "T:", time()-start
