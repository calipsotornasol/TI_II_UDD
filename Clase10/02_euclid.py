def gcd(p, q):
    if q == 0:
        return p
    return gcd(q, p % q)
    
p = int(input('Ingrese un numero:'))
q = int(input('Ingrese un numero:'))

divisor = gcd(p, q)

print("El maximo comun divisor es:", str(divisor))
