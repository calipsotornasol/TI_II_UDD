def int2bin(n):
    binarynumber=""

    if (n!=0):
        while (n>=1):
            if (n %2==0):
                binarynumber=binarynumber+"0"
                n=n/2
            else:
                binarynumber=binarynumber+"1"
                n=(n-1)/2

    else:
        binarynumber="0"

    return binarynumber[::-1] #Retornar el binarynumber invertido
 
n= int(input("Ingrese un número para convertir a binario:"))
print(int2bin(n))
