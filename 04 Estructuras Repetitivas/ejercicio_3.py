# Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.

primer_numero = int(input("Ingrese el primer numero: "))
segundo_numero = int(input("Ingrese el segundo numero: "))
suma = 0

if primer_numero > segundo_numero:  
    numero_mayor = primer_numero
    numero_menor = segundo_numero
elif primer_numero == segundo_numero:
    print("La diferencia es 0")
    exit()
else:
    numero_mayor = segundo_numero
    numero_menor = primer_numero

for i in range(numero_menor + 1, numero_mayor):
    suma += i
    
print(f"La suma entre los valores brindados es: {suma}")