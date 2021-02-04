#estructuras que extraen valores de una funcion y se almacenan en objetos iterables
#estos valores se almacenan de uno en uno
''' cada vez que un generador almacena un valor, 
este permanece en un estado pausado hasta que se solicita el siguiente.
Caracteristica conocima como suspension de estado'''

'''def generaPares(limite):

	num=1
	miLista=[]

	while num<limite:
		miLista.append(num*2)

		num+=1

	return miLista

print(generaPares(10))'''

def generadorPares(limite):
	num=1

	while num<limite:

		yield num*2

		num=num+1

devuelvePares=generadorPares(10)

print(next(devuelvePares))

print("Aqui podria ir mas codigo...")

print(next(devuelvePares))

print("Aqui podria ir mas codigo...")

print(next(devuelvePares))




