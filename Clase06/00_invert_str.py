#Método 1
s1= '' #str vacío, no es un espacio
s2='Hola'
for c in s2:
	s1 = c + s1
print(s2, 'invertido:', s1)
print('\n')

#Método 2

s3='Hola'
print(s3, 'invertido:', s3[::-1])