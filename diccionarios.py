midiccio = {"Alemania":"Berlin", "Francia":"París", "Reino Unido":"Londres","España":"Madrid"}
#indicar clave para imprimir valor
print(midiccio["España"])

#imprimr diccionario entero
print(midiccio)

#Agregar valor a diccionario
midiccio["Argentina"]="Roma"
print(midiccio)

#Corregir, se sobreescribe al tener misma clave
midiccio["Argentina"]="Buenos Aires"
print(midiccio)

#Eliminar elementos
del midiccio["Reino Unido"]
print(midiccio)

#Combinacion de tipos de datos
midiccio2 = {"Alemania":"Berlin", 23:"Jordan", "Mosqueteros":3}
print(midiccio2)

#Tupla a diccionario
mitupla=["España", "Francia", "Reino Unido", "Alemania"]
midiccio3={mitupla[0]:"Madrid",mitupla[1]:"Paris",mitupla[2]:"Londres",mitupla[3]:"Berlin"}
print(midiccio3)

#Tupla dentro de un diccionario
midiccio4={23:"Jordan","Nombre":"Michael","Equipo":"Chicago","anillos":[1991,1992,1993,1996,1997,1998]}
print(midiccio4)
print(midiccio4["Equipo"])
print(midiccio4["anillos"])


#metodo keys,values,len
print(midiccio.keys())
print(midiccio.values())
print(len(midiccio))
