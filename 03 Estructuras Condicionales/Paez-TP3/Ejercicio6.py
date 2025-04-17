# Escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si hay sesgo positivo, negativo o no hay sesgo.
# Imprimir el resultado por pantalla.

from statistics import mode, median, mean
import random

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

print(f"Media: {media:.2f}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")

if media > mediana and mediana > moda:
    print("Hay sesgo positivo")
elif media < mediana and mediana < moda:
    print("Hay sesgo negativo")
elif media == mediana and mediana == moda:
    print("No hay sesgo")
else:
    print("No hay un sesgo definido")