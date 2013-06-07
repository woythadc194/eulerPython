"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
"""

def letters(n):
    if len(n)==1:
        return ones(int(n))
    if len(n)==2:
        return tens(int(n))
    if len(n)==3:
        return hundreds(int(n))
    if len(n)==4:
        place = ones(int(n)/1000)
        print 'thousand',
        return 8 + place
        
def ones(n):
    if n==0:
        return 0
    if n==1:
        print 'one',
        return 3
    if n==2:
        print 'two',
        return 3
    if n==3:
        print 'three',
        return 5
    if n==4:
        print 'four',
        return 4
    if n==5:
        print 'five',
        return 4
    if n==6:
        print 'six',
        return 3
    if n==7:
        print 'seven',
        return 5
    if n==8:
        print 'eight',
        return 5
    if n==9:
        print 'nine',
        return 4
    
def tens(n):
    if 10<=n and n<=19:
        if n==10:
            print 'ten',
            return 3
        if n==11:
            print 'eleven',
            return 6
        if n==12:
            print 'twelve',
            return 6
        if n==13:
            print 'thirteen',
            return 8
        if n==14:
            print 'fourteen',
            return 8
        if n==15:
            print 'fifteen',
            return 7
        if n==16:
            print 'sixteen',
            return 7
        if n==17:
            print 'seventeen',
            return 9
        if n==18:
            print 'eighteen',
            return 8
        if n==19: #an online dictionary spelled this ninteen, delaying my answer
            print 'nineteen', 
            return 8
    else:
        if n/10==0:
            return ones(n%10)
        if n/10==2:             
            print 'twenty',
            return 6 + ones(n%10)
        if n/10==3:
            print 'thirty',
            return 6 + ones(n%10)
        if n/10==4:
            print 'forty',
            return 5 + ones(n%10)
        if n/10==5:
            print 'fifty',
            return 5 + ones(n%10)
        if n/10==6:
            print 'sixty',
            return 5 + ones(n%10)
        if n/10==7:
            print 'seventy',
            return 7 + ones(n%10)
        if n/10==8:
            print 'eighty',
            return 6 + ones(n%10)
        if n/10==9:
            print 'ninety',
            return 6 + ones(n%10)

def hundreds(n):
    place = ones(n/100)
    print 'hundred',
    place += 7
    
    if n%100>0:
        print 'and',
        place += 3
        return place + tens(n%100)
    else:
        return place

total = 0
for i in range(1,1001):
    current = letters(str(i))
    total += current
    print current
print total
