# lista con valores desde teclado
L = [] #lista vacÃ­a
N=3
for i in range(N):
    v = int(input("Ingrese elemento" + "\n"))
    L.append(v)

print('Imprimir elementos en lista', '\n')
# imprimir elementos en lista
for elem in L:
    print(elem)
 
print('Imprimir elementos en lista', '\n')
# imprimir elementos en lista (otra forma)
for i in range(N):
    print(L[i])
    

print('Maximo', '\n')

# encontrar el ma¡ximo 
maxi = L[0]
for elem in L:
    if elem > maxi:
        maxi = elem
print("El maximo es:", maxi)

print('Minimo', '\n')

# encontrar el mi­nimo
mini = L[0]
for elem in L:
    if elem < mini:
        mini = elem
print("El minimo es:",mini)

# promedio
suma = 0.0
for elem in L:
    suma = suma + elem
prom = suma/N

# copiar lista
L2 = []
for elem in L:
    L2.append(elem)

# invertir elementos de la lista
for i in range(N):
    temp = L[i]
    L[i] = L[N-i-1]
    L[N-i-1] = temp

# insertar elemento al final
L.append(33)
