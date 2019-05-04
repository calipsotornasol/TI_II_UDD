from random import random

def fillrandom(matrix, rows, cols):
    for i in range(rows):
        for j in range(cols):
            matrix[i][j] = random()

rows = 3
cols = 4

matrix = [ [0]*cols ]*rows

fillrandom(matrix, rows, cols)

print(matrix)
