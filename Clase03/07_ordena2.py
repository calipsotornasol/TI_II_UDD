# ingresa tres números enteros por teclado
# separados por un espacio
a = int(input("Ingresa el primer numero: "))
b = int(input("Ingresa el segundo numero: "))
c = int(input("Ingresa el tercer numero: "))
if b < a:
    a, b = b, a
if c < a:
    a, c = c, a
if c < b:
    c, b = b, c
print(a)
print(b)
print(c)
