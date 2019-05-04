def fibonacci(N):
    if N < 0:
        raise ValueError("N no debe ser negativo")
    L = []
    a, b = 0, 1
    while len(L) < N:
        a, b = b, a + b
        L.append(a)
    return L
    
fibonacci(-10)
