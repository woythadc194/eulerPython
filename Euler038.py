"""
Take the number 192 and multiply it by each of 1, 2, and 3:

192  1 = 192
192  2 = 384
192  3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n  1?
"""
from time import time
start = time()

def is_pandig_1_9(s):
    s = str(s)
    if len(s)!=9:
        return False
        
    digits = []
    for i in range(9):
        digits.append(0)
        
    for l in s:
        digits[int(l)-1]=1
    if 0 in digits:
        return False
    return True

greatest = 0
n = 2
while n<10000: #Because len(concat) of x=1 and x=2 is greater than 9
    concat = ''
    x=1
    while len(concat)<9:
        concat += str(n*x) 
        x += 1
    if is_pandig_1_9(concat):
        if greatest<int(concat):
            greatest = int(concat)
    n+=1
print "A:", greatest
print"T:", time()-start        
