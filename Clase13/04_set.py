print("Imprimiendo un set")
A = {1, 2, 2, 3}
print('A:', A)

print('\n')

print("Consultando por un valor")
print('2 in A?:', 2 in A)
print('\n')


print("Anadiendo un valor")
A.add(99)
print('A.add(99):', A)
print('\n')

print("Removiendo un valor")
A.remove(2)
print('A.remove(2):', A)
print('\n')

print("Creando un set con valores de diferente tipo")
B = set([1, 2, 3, 'hola'])
print('B:', B)
print('\n')

print("Algunas operaciones")
print("Intersección")
print('A ∩ B:', A.intersection(B))
print('A ∩ B:', A & B)
print('\n')

print("Union")
print('A ∪ B:', A.union(B))
print('A ∪ B:', A | B)
print('\n')

print("Diferencia")
print('A - B:', A.difference(B))
print('A - B:', A - B)
