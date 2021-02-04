'''EJERCICIO 4: 
    Solicitar al usuario que ingrese números enteros positivos y, 
    por cada uno, imprimir la suma de los dígitos que lo componen. 
    La condición de corte es que se ingrese el número -1. Al finalizar, 
    mostrar cuántos de los números ingresados por el usuario fueron 
    números pares.'''

numero = int(input("Ingrese un numero entero positivo: "))
contador = 0

while numero!=-1:
	if numero%2==0:
		contador+=1
	suma = 0
	while numero >=10:
		suma =suma+ (numero%10)
		numero = numero//10   
	suma = suma + numero 
    print("La suma de los digitos es ",suma)
    num = int(input("Ingrese otro número\n"))
print("Cantidad de números pares: ", contador)





