"""
The nth term of the sequence of triangle numbers is given by, tn = .5n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

Using 042.txt, a 16K text file containing nearly two-thousand common English words, how many are triangle words?
"""

from time import time
start = time()

def get_vals(line):
    row = []
    token = ''
    for l in line:
        if l != '"' and l!=',':
            token += l
        else:
            if token != '':
                row.append(token)
            token = ''
    row.append(token)
    return row
    
my_file = open("042.txt")
words = get_vals(my_file.readline())
my_file.close()

tri_num = []

for n in range(1,20):
    tri_num.append(int(.5*n*(n+1)))
    
total = 0
for word in words:
    word_val = 0
    for l in word:
        word_val += (ord(l)-ord('A')+1)
    if word_val in tri_num:
        total += 1

print "A:", total
print "T:", time()-start
