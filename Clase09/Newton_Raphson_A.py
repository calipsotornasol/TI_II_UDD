from math import sqrt
z = int(input("Ingrese un numero: "))
n = int(input("Ingrese numero de iteraciones: "))

##Parte a
print('Parte a' + '\n')
x=n*[0] 
x[0] = z/2
error=n*[0] 
error[0]=abs(x[0]-z)/x[0]

print(str(0)+ ": " + "Valores aproximados para la raiz de " + str(z)+": "+ str(x[0]) + " Error: " + str(error[0]))
for i in range(1, n):
	x[i] = 1/2*(x[i-1] + z/x[i-1])
	error[i] = abs(x[i]-x[i-1])/x[i]
	print(str(i)+ ": " + "Valores aproximados para la raiz de " + str(z)+": "+ str(x[i]) + " Error: " + str(error[i]))

print('\n')

