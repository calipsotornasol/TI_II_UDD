from math import sqrt
z = int(input("Ingrese un numero: "))
n = int(input("Ingrese numero de iteraciones: "))

##Parte a
print('Parte a' + '\n')

x0 = z/2
error=abs(x0-z)/x0

print(str(0)+ ": " + "Valores aproximados para la raiz de " + str(z)+": "+ str(x0) + " Error: " + str(error))
for i in range(1, n):
    x = 1/2*(x0 + z/x0)
    error = abs(x-x0)
    x0=x
    print(str(i)+ ": " + "Valores aproximados para la raiz de " + str(z)+": "+ str(x) + " Error: " + str(error))

print('\n')

