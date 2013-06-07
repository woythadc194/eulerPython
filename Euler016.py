"""
215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?
"""
SCALE = 1000
x = str(2**SCALE)
total = 0
for l in x:
    total += int(l)
print total
