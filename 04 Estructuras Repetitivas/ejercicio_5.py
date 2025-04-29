# Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. 
# Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.


import random

numero_aleatorio = random.randint(0, 9)
numero_usuario = int(input("Ingrese un numero: "))
intentos = 1

while numero_usuario != numero_aleatorio:
    numero_usuario = int(input("Ingrese otro numero: "))
    intentos += 1

print(f"¡Felicidades, el numero era {numero_aleatorio} y te llevo {intentos} intentos adivinarlo!")