
import math

i=1

while i<=10:
	print("Ejecucion "+ str(i))
	i+=1

print("Terminó la ejecución")


#While indeterminado
edad=int(input("Ingrese su edad: "))

while edad<0 or edad>120:
	if edad<0:
		edad=int(input("La edad no puede ser negativa, intente nuevamente: "))
	elif edad>120:
		edad=int(input("La edad no puede pasar de 100, intente nuevamente: "))

print("Su edad es: " + str(edad))




print("Programa de cálculo de Raíz cuadrada")
numero=int(input("Introduce un numero por favor: "))

intentos=0

while numero<0:
	print("No se puede hallar la raiz de un numero negativo")

	if intentos==2:
		print("Has consumido demasiados intentos. El programa ha finalizado")
		break;
	numero=int(input("Introduce un numero por favor: "))
	if numero<0:
		intentos=intentos+1

if intentos<2:
	solucion=math.sqrt(numero)
	print("La raiz cuadrada de",numero,"es",solucion)




















