# Escribir un programa que solicite una frase o palabra al usuario. 
# Si el string ingresado termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por pantalla 
# En caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.

frase = input("Escriba una frase: ")
ultimaLetra = frase[-1].lower()
vocales = "aeiou"

if ultimaLetra in vocales:
    print(f"{frase}!")
else:
    print(f"{frase}")