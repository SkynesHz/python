mitupla = ("Juan",13,1,1995)

#empaquetado de tupla
tupla_sin_parent = "Juan", 14, 21


lista = ["Pedro", "Ricky", 14]
#convertir tupla en lista con metodo list
milista = list(mitupla)
print(milista)
print(mitupla)

#convertir lista en tupla con metodo tuple
listupla = tuple(lista)
print(listupla)

#in para ver si un elemento se encuentra en la tupla
print("Juan" in mitupla)

#count para saber cuantos veces aparece un elemento
print(mitupla.count(13))

#len para saber longitud de la tupla
print(len(mitupla))


#tupla unitaria
tupla_unitaria = ("Juan",)
print(len(tupla_unitaria))


#desempaquetado de tuplas
nombre, dia, mes, anio = mitupla
print(nombre)
print(dia)
print(mes)
print(anio)

print(mitupla.index("Juan"))


