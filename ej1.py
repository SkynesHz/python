#Suponiendo que la contraseña es 123123

contra = input("Ingrese su contraseña: ")
intentos = 4
while (contra != "123123") & (intentos > 0):
    contra = input("Ingrese nuevamente la contraseña: ")
    intentos = intentos - 1



if intentos>0:
    print("Bienvenido")
else:
    print("Su cuenta ha sido bloqueada")

