from math import sqrt
z = int(input("Ingrese un numero: "))

print('Parte b' + '\n')

x0=z/2

error=x0

while error > 0.00001:
	x = 1/2*(x0 + z/x0)
	error = abs(x-x0)/x
	x0 = x

print("Valor aproximado para la raiz de " + str(z) + ":\n")
print(x)
