# Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa función para calcular y mostrar 
# en pantalla el factorial de todos los números enteros entre 1 y el número que indique el usuario

# Funcion factorial

def factorial(num):
    if num == 0: 
        return 1 
    else: 
        return num * factorial(num - 1)
        print(f"El factorial entre 1 y {num} es {factorial()}")

# Solicitud de entrada al usuario

numero_usuario = int(input("Ingrese un numero: "))

# Ciclo para que el print funcione correctamente 

for i in range(1, numero_usuario + 1):
    print(f"El factorial de {i} es {factorial(i)}")