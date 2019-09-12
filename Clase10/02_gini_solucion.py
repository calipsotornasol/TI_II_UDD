pais=[]
gini=[]

#Leyendo archivo
with open("gini_by_country.csv") as file:
    for line in file:
        s=line.split(',')[0] #Paso texto antes de la coma a una lista
        pais.append(s)
        g=line.split(',')[1].strip() #Paso texto despues de la coma a una lista
        gini.append(float(g))

gini_sort=gini.copy() #Copio la lista gini para ordenarla
gini_sort.sort(reverse=True) #Ordeno la copia de la lista gini

#print(gini_sort)
min_gini=min(gini_sort[:5]) #Busco el minimo del indices gini dentro de los 5 indices mas altos
#print(min_gini)


#Opcion 1. Imprime los que son mayores o iguales al minimo de los 5 mejores. No entrega un ranking
print('Solucion 1:')
print('Los paises con más desigualdad son:' + '\n')
for i in range(len(pais)):
    if gini[i]>=min_gini:
        print(pais[i] + ' ', str(gini[i]))


#Opcion 2. Imprime los top-5 en desigualdad en orden
index_gini = len(gini)*[0] #Creo una lista para guardar los indices
for i in range (len(gini)):
    index_gini[i]=gini.index(gini_sort[i])
#print(index_gini[:5])

print('Solucion 2')
print('Los paises con más desigualdad son:' + '\n')
for i in range(5):
    print(pais[index_gini[i]]+ ' ' + str(gini[index_gini[i]]))

