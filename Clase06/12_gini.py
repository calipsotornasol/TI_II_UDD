#Abriendo archivo
f = open('gini_by_country.csv','r')

#Imprimiendo
for l in f:
    print(l)
f.close()


