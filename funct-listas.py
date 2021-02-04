mi_lista = [1,2,3,4,5,6]
otra_lista = [10,11,12,13]

len(mi_lista) #Obtener longitud de la lista

#Recorrer lista

for index in range(0,len(mi_lista)):
	print(lista[index])

for elemento in mi_lista:
	print(elemento)

#Agregar elemento a lista
mi_lista.append(7)

mi_lista.insert(8)

#Agregar todos los elementos de otra lista
mi_lista.extend(otra_lista)


#Obtener sublistas(slicing)
lista_cortada = mi_lista[1:3]
#se puede omitir el primer numero :3 y comenzará desde el inicio
#se puede omitir el segundo numero 3: y comenzará desde el tercero hasta el final
#si solo se ponen los dos puntos ":" tomará toda la lista


#Copiar lista
copia = mi_lista[:]
copia = mi_lista.copy()


#Ordenar lista
mi_lista.sort()

mi_lista.sort(reverse=True)

#Invertir lista
mi_lista.reverse()

#Saber si un elemento se encuentra en la lista
print(1 in mi_lista)

#Saber cuantas veces se encuentra un elemento en una lista
mi_lista.count(1)

#Conocer el indice de un elemento
print(lista.index(4))


#Eliminar elementos de una lista
del mi_lista[3]
del otra_lista[1:3]

copy.remove(5)

elemento_quitado = copy.pop(2) #Eliminar el elemento en el indice y lo retorna

#Devolver el minimo
minimo = mi_lista.min()

#Devolver el maximo
maximo = mi_lista.max()


#Devolver suma entre sus elementos
suma = mi_lista.sum()




