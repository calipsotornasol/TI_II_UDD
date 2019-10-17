def alumno_nota_max():
    f = open('notas_prograudd.txt','r')
    nombres=[]
    notas=[]
    
    for l in f:
        L=l.split()     
        nombres.append(L[0])
        notas.append(L[1])
    f.close()
    
    nota_max=max(notas)
    nombres_nota_max=[]
    
    for i in range(len(notas)):
        if notas[i] == nota_max:
            nombres_nota_max.append(nombres[i])
            
    return nombres_nota_max
    
    
def nota_max():
    f = open('notas_prograudd.txt','r')
    nombres=[]
    notas=[]

    for l in f:
        L=l.split()     
        nombres.append(L[0])
        notas.append(L[1])
    f.close()
    
    nota_max=max(notas)
    
    return nota_max 
    
def nota_min():
    f = open('notas_prograudd.txt','r')
    nombres=[]
    notas=[]

    for l in f:
        L=l.split()     
        nombres.append(L[0])
        notas.append(L[1])
    f.close()
    
    nota_min=min(notas)
    
    return nota_min 
    
    
def promedio():
    f = open('notas_prograudd.txt','r')
    nombres=[]
    notas=[]
    
    for l in f:
        L=l.split()     
        notas.append(float(L[1]))
    f.close()
            
    return round(sum(notas)/len(notas),2)
    
def notas_bajo(n):
    f = open('notas_prograudd.txt','r')
    nombres=[]
    notas=[]
    
    for l in f:
        L=l.split() 
        nombres.append(L[0])
        notas.append(float(L[1]))
    f.close()
    
    notas_aux=[]
    for i in range(len(notas)):
        if notas[i]<=n:
            notas_aux.append(nombres[i] + ' ' + str(notas[i]))
            
    return notas_aux
    
   
print('Nota max', alumno_nota_max(),nota_max(), '\n')
print('Nota min', nota_min(), '\n') 
print('Promedio', promedio(), '\n')
print('Notas menores o iguales a 4.0', notas_bajo(4.0))

