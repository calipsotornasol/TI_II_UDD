#09_while
numero = int(input("Por favor, escriba un número positivo: "))
while numero < 0:
    print("¡Error!¡Usted ha escrito un número negativo! Por favor inténtelo de nuevo")
    numero = int(input("Por favor, escriba un número positivo: "))
print("El numero ingresado es correcto")
