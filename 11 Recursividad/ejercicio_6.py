# Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un número entero positivo y devuelva 
# la suma de todos sus dígitos.
# No se puede convertir el número a string.
# Usá operaciones matemáticas (%, //) y recursión.

# Declaracion de variable

def suma_digitos(num):
    if num < 10:
        return num
    elif num <= 0:
        print("Error")
        return None
    else:
        return num % 10 + suma_digitos(num // 10)

# Entrada del usuario

num = int(input("Ingrese un numero: "))

# Salida al usuario

print(suma_digitos(num))

