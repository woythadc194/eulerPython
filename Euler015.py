"""
Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20x20 grid?
"""

SCALE = 2
SCALE += 1      #corners of the cells, not the cells themselves (1cube=2corners)
matrix = []

def print_matrix(martix):
    for x in range(len(matrix[0])):
        for y in range(len(matrix)):
            print matrix[x][y],
        print '\n'

first_row = [0]
for z in range(SCALE-1):
    first_row.append(1)
matrix.append(first_row)
other_rows = [1]
for x in range(SCALE-1):
    other_rows.append(0)
for y in range(SCALE-1):
    matrix.append(other_rows)
    
print_matrix(matrix)
print '\n'

for x in range(1,SCALE):
    for y in range(1,SCALE):
        matrix[x][y] = matrix[x-1][y] + matrix[x][y-1]
print_matrix(matrix)
print matrix[SCALE-1][SCALE-1]
