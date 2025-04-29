# Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. 
# El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.

numero_usuario = int(input("Ingrese un numero: "))
suma = 0

while numero_usuario != 0:
    suma = numero_usuario + suma
    print(f"El total acumulado es {suma}")
    numero_usuario = int(input("Ingrese un numero: "))

print(f"El total acumulado es: {suma}")
