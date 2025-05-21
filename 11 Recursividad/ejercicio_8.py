# Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un número entero positivo (numero) 
# y un dígito (entre 0 y 9), y devuelva cuántas veces aparece ese dígito dentro del número.

# Declaracion de funcion

def contar_digito(numero, digito):
    if numero == 0:
        return 0
    if numero % 10 == digito:
        return 1 + contar_digito(numero // 10, digito)
    else:
        return contar_digito(numero // 10, digito)

        

# Solicitud de entrada al usuario

numero = int(input("Ingrese un numero entero: "))
digito = int(input("Ingrese un digito: "))

# Salida al usuario

print(f"El digito {digito} aparece {contar_digito(numero, digito)} veces en el numero {numero}")

