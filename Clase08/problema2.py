#Función random.uniform
from random import uniform
def rand2d():
    x=uniform(-0.5, 0.5)
    y=uniform(-0.5, 0.5)
    return x, y

#Inicializamos variables
N = int(input("Ingrese N: "))
i=0
n=0
x, y = rand2d()


#Comienza el ciclo
while i<N:
    if x**2+y**2 < 1/4: #Condicion 1
        n = n+1
    i=i+1 #
    x, y = rand2d()

pi = 4*n/N
print("Pi es aproximadamente ", pi)