def fibonacci(N, a=0, b=1):
    L = []
    while len(L) < N:
        a, b = b, a + b
        L.append(a)
    return L
    
#print(fibonacci(10))
print(fibonacci(10,b=3, a=1))

