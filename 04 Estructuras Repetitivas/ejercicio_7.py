# Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.

suma = 0
numero_usuario = int(input("Ingrese un numero entero positivo: "))

if numero_usuario == 0:
    print("Ingrese un numero diferente a 0")
elif numero_usuario < 0:
    print("Ingrese un numero positivo")

for i in range(0, numero_usuario + 1):
    suma += i
    
print(f"La suma entre los valores brindados es: {suma}")


