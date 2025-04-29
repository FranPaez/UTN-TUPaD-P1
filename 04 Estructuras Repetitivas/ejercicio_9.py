# Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores. 
# (Nota: puedes probar el programa con una cantidad menor, pero debe poder procesar 100 números cambiando solo un valor).


acumulador = 0

for i in range(100): # Se deja el range en 100 porque asi lo pide el ejercicio, para verificar con menor cantidad se debe disminuir.
    numero_usuario = int(input("Ingrese un numero: "))
    acumulador = acumulador + numero_usuario

media = acumulador / 100

print(f"La media es: {media}")