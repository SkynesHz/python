#Definicion de listas
miLista=["Hola", "Mundo", "Juan", 10, True, 15.4]

#Imprimir toda la lista
print(miLista[:])

#Imprimir elemento especifico de una lista
print(miLista[1])

#Imprimir un rango de indices
print(miLista[0:3])

#Agregar elemento al final de la lista
miLista.append("Sandra")
print(miLista[:])

#Agregar elemento en la posicion indicada por el primer parametro
miLista.insert(2, "Willy")
print(miLista[:])

#Concatenar lista del paramatro a la lista original
miLista.extend(["Jorge", "Marta"])
print(miLista[:])

#Devolver indice el elemento pasado como parametro
print(miLista.index("Jorge"))

#True o false si el elemento se encuentra en la lista
print("Marta" in miLista)

#Quitar elemento de lista
miLista.remove(True)
print(miLista[:])

#Eliminar ultimo elemento
miLista.pop()
print(miLista[:])


#Concatenar listas y alamcenarla en otra
miLista2=["Ricardo", "Luciano"]

miLista3=miLista+miLista2
print(miLista2)

#Operador multiplicacion en lista
#Repite la lista
miLista4=["Pedro","Sanchez"]*3
print(miLista4[:])