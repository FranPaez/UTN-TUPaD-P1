# Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. 
# Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.


numero_usuario = int(input("Ingrese un el numero: "))

if numero_usuario <= 0:
    print("Ingrese un numero valido")
else: 
    numero_invertido = str(numero_usuario)[::-1]
    print(f"El numero invertido es: {numero_invertido}")
