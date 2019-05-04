frutas = ("manzana", "platano", "naranja")
print(frutas)

#Accediendo a un elemento
print("Imprimiendo el primer elemento")
print(frutas[0])


print('\n')
      
#Iterando
print("Imprimiendo los elementos uno a uno:")
for fruta in frutas:
  print(fruta)

#Verificando si existe algun elemento en la tupla
print('\n')
print("Imprimiendo los elementos uno a uno:")
if "manzana" in frutas:
      print("Sí, manzana esta en frutas")

print('\n')

#Largo de la tupla
print("El largo de la tupla frutas es:")
print(len(frutas))

#Anadir un elemento a una tupla
print("Anandiendo un elemento a una tupla")
frutas[3] = "frutilla" # Error
print(frutas)
