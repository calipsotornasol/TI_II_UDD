from math import sqrt
z = int(input("Ingrese un numero para estimar su raiz: "))
n = int(input("Ingrese numero de iteraciones: "))

#Problema 1

print('Parte a' + '\n')

x0 = z/2
for i in range(0, n):
    x = 1/2*(x0 + z/x0)
    error = abs(x-x0)/x0
    x0=x
    print(str(i)+ ": " + "Valores aproximados para la raiz de " + str(z)+": "+ str(x) + " Error: " + str(error))

print('\n')

