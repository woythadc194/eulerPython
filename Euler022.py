"""
Using 022.txt, a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 
3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938  53 = 49714.

What is the total of all the name scores in the file?
"""

def get_vals(line):
    row = []
    word = ''
    for l in line:
        if l != '"' and l!=',':
            word += l
        else:
            if word != '':
                row.append((word))
            word = ''
    return row

my_file = open('022.txt', 'r')
names = sorted(get_vals(my_file.readline()))
my_file.close()

def nameval(index, name):
    mini_total = 0
    for l in name:
        mini_total += (ord(l)-ord('A')+1)
    return mini_total * index

total = 0
for index, name in enumerate(names):
    mini_total = nameval(index+1, name)
    print name + ":", index+1, '*', mini_total/(index+1), '=', mini_total
    total += mini_total

print 'total:',total
