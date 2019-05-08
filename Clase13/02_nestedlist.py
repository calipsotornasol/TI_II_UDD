from random import random
#Inicializando matriz de ceros
rows = 3
cols = 4
matrix = []

for i in range(rows):
    matrix.append([0]*cols)

#Creando una funcion para crear una matriz con numeros al azar
def fillrandom(matrix, rows, cols):
    for i in range(rows):
        for j in range(cols):
            matrix[i][j] = random()

print("Matriz de ceros")
print(matrix)
print('\n')

print("Matriz random")
fillrandom(matrix, rows, cols)

print(matrix)
