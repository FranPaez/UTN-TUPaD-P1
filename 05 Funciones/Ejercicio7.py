# Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y devuelva una tupla 
# con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.

# Declaracion de funciones

def operaciones_basicas(num1, num2):
    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2
    division = num1 / num2
    return (suma, resta, multiplicacion, division)

# Programa principal

# Pedido de variables al usuario

a = int(input("Ingrese un numero: "))
b = int(input("Ingrese otro numero: "))

# Se guarda los valores en una tupla, como pide el ejercicio 

suma, resta, multiplicacion, division = operaciones_basicas(a, b)

# Mostramos resultados 

print(f"Esto es el resultado de realizar suma, resta, multiplicacion y division con {a} y {b}: ")
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")
