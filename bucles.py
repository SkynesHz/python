for i in [1,2,3]:
	print("Hola",i)


for j in ["Pildoras", "Informaticas", 3]:
	print("Hola", end=" ") #end para indicar como terminar el print

print()


#range 

for i in range(5):
	print("Hola",i)


#Unir texto con variable
for i in range(5):
	print(f"valor de la variable {i}")

print()

#empezar de un numero determinado
for i in range(5,10):
	print(f"valor de la variable {i}")

print()
#empezar de un numero determinado de con incremento determinado
for i in range(5,50,3):
	print(f"valor de la variable {i}")



valido=False

email=str(input("Introduce tu email: "))

for i in range(len(email)):

	if email[i]=="@":
		valido=True

if valido:
	print("El email es correcto")
else:
	print("Email incorrecto")



