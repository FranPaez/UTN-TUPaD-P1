# Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada. 
# Posteriormente, muestra la serie completa hasta la posición que el usuario especifique.

# Declaracion de funcion

def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)

# Solicitud de entrada al usuario

numero_usuario = int(input("Ingrese un numero por favor: "))

# Salida al usuario

print("Serie de Fibonacci:")
for i in range(numero_usuario + 1):
    print(fibonacci(i), end=" ")




