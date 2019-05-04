#Ingreso valores para z y n
z = float(input("Ingrese z: "))
n = int(input("Ingrese n: "))

print('\n')

#Inicializar variable S
S = 0

if abs(z)<1: #Suma para z <1
    for k in range(1, n+1):
        S = S + z**k
    print('S es igual a: '+ 'S' + '\n')
else:
    print("|z| debe ser menor a 1")

#Comparando resultados
print('Iniciando test' + '\n')
R = (1-z**n)/(1-z)
print('R es igual a: ' + '{:.2f}'.format(R)+'\n')

if R/S == 1:
    print("La serie S es igual al resultado R")
else:
    print("La serie S es diferente al resultado R")
