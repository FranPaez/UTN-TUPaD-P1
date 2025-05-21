# Crear una función recursiva en Python que reciba un número entero positivo en base decimal y devuelva su representación 
# en binario como una cadena de texto.

# Declaracion de funcion

def binario_a_decimal(num):
    if num == 0:
        return ""
    else: 
        return binario_a_decimal(num // 2) + str(num % 2)



# Solicitud de entrada al usuario

num = int(input("Ingrese el numero entero: "))

# Ciclo para que el print funcione correctamente 

print(binario_a_decimal(num))
