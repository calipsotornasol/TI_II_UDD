a = int(input('ingrese a: '))
b = int(input('ingrese b: '))
if a > b:
    # Cuando la condición se cumple
    print('a es mayor que b')
else:
    if a < b:
        # Cuando la condición se cumple
        print('a es menor o igual que b')
    else:
        # Cuando ni la primera, ni la segunda
        # condición se cumple
        print('a es igual a b')
