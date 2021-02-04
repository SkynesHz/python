coordenadas = {"x":34, "y": 23, "z":45}
agenda_telefonica = {
"Sandra":456773,
"Pedro":3784758,
"Lorena":483758,
"Juan":578493
}
seleccion_futbol = {
1:"Sergio Almirón",
2:"Sergio Batista",
3:"Ricardo Enrique Bochini",
4:"Claudio Borghi",
5:"José Luis Brown",
6:"Daniel Passarella",
7:"Jorge Burruchaga",
8:"Néstor Clausen",
9:"José Luis Cuciuffo",
10:"Diego Maradona",
11:"Jorge Valdano"
}
alumno = { "nombre": "Marcos", "materias":["biología", "matemáticas", "diseño"]}

print(coordenadas["x"])
print(agenda_telefonica["Sandra"])
print(seleccion_futbol[10])

#Agregar elementos
usuario = { "nombre":"Juan", "edad":23 }
usuario["apellido"] = "Perez"
usuario.setdefault("comida_favorita","ninguna")

#Obtener elemento
usuario[nombre]
color = usuario.get("color_favorito")
print(color)
color = usuario.get("color_favorito","no tiene color favorito") #El segundo parametro es lo que devuelve en caso de no encontrar la clave

#Recorrer diccionarios
diccionario = {"a":11, "b":22, "c":33, "d":44}
for key in diccionario:
	print("La clave es: ",key)
	print("Su valor es: ",diccionario[key])

diccionario.items() #devuelve una lista de tuplas que cotiene el par clave:valor

for key,value in diccionario.items():
	print(key,":",value)

#Verificar si una clave se encuentra en el diccionario, podemos usar el operador in
"a" in diccionario #devuelve true o false


#Eliminar par clave:valor
persona = {"nombre":"Marta", "genero":"F"}
print(persona)
del persona["genero"]
print(persona)

#Con pop() se elimina el par clave:valor y devuelve el valor quitado
quitado = diccionario.pop("a")
print(quitado)
valor = diccionario.pop("a", "valor no encontrado")

#Eliminar un diccionario completo
diccionario.clear()

#Actualizar diccionario con elementos de otro
diccionario_uno = {"a":100, "b":456, "c":45, "d":88}
diccionario_dos = {"d":110, "f":66, "g":45, "h":99 }
diccionario_uno.update(diccionario_dos)
#si hay claves repetidas el valor se actualiza al del diccionario pasado como parametro
print(diccionario_uno) 

#Saber cantidad de elementos de un diccionario
diccionario = {"hola":"hello", "chau":"bye", "cinco":"five",
"manzana":"apple"}
len(diccionario)

#Obtener lista con las claves
diccionario.keys()

#Recibir lista con valores del diccionario
diccionario.values()


#Si necesitamos listas podemos crearlas a partir de estas vistas con la función list(), o si
#necesitamos tuplas con tuple()
diccionario = {"a":10,"b":20}
valores = diccionario.values()
print(valores)
lista = list(valores)



