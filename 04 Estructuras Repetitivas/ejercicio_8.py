# Escribe un programa que permita al usuario ingresar 100 números enteros. 
# Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son negativos y cuántos son positivos. 
# (Nota: para probar el programa puedes usar una cantidad menor, pero debe estar preparado para procesar 100 números con un solo cambio).


numeros_positivos = 0
numeros_negativos = 0
numeros_pares = 0
numeros_impares = 0

for i in range(100): # Se deja el range en 100 porque asi lo pide el ejercicio, para verificar con menor cantidad se debe disminuir.
    numero_usuario = int(input("Ingrese un numero entero: "))

    if numero_usuario % 2 == 0:
        numeros_pares += 1
    else:
        numeros_impares += 1

    if numero_usuario > 0:
        numeros_positivos += 1
    elif numero_usuario < 0:
        numeros_negativos += 1

print(f"La cantidad de numeros positivos es: {numeros_positivos}")
print(f"La cantidad de numeros negativos es: {numeros_negativos}")
print(f"La cantidad de numeros pares es: {numeros_pares}")
print(f"La cantidad de numeros impares es: {numeros_impares}")