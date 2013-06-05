"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
SCALE = 20
x=SCALE
i=SCALE
while i>0:
    if x%i==0:
#        print "%d / %d = 0" % (x,i)
        i-=1
    else:    
        x+=SCALE
        i=SCALE
print x
