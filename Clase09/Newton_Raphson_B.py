##Parte b

from math import sqrt
z = int(input("Ingrese un numero: "))
n = int(input("Ingrese numero de iteraciones: "))

##Parte a


print('Parte b' + '\n')

x0=z/2
error=abs(x0 - z)/x0

while error > 0.00001:
	x = 1/2*(x0 + z/x0)
	error = abs(x-x0)/x
	x0 = x

print("Valor aproximado para la raiz de " + str(z) + ":\n")
print(x)
