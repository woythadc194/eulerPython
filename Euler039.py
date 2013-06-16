"""
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p<=1000, is the number of solutions maximised?
"""
from time import time
start = time()

perims = []
for i in range(1001):
    perims.append(0)

for a in range(1,500):
    for b in range(1,500):
        for c in range(1,500):
            if a+b+c<=1000:
                if a**2 + b**2 == c**2:
                    perims[a+b+c] += 1
                
largest = 0
finalP = 0
for index, p in enumerate(perims):
    if largest<p:
        largest = p
        finalP = index
print "A:", finalP
print "T:", time()-start
