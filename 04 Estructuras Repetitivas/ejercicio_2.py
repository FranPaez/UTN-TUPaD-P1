# Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.

numero_usuario = int(input("Ingrese un número: "))

if numero_usuario <= 0:
    print("Ingrese un número mayor a 0")
elif numero_usuario < 10:
    print("El número contiene solo 1 dígito.")
else:
    digito = 1 
    while numero_usuario >= 10:
        numero_usuario = numero_usuario // 10
        digito += 1
    print(f"El número contiene {digito} dígitos.")



    
    
    