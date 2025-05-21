# Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n bloques, en el siguiente nivel 
# uno menos (n - 1), y así sucesivamente hasta llegar al último nivel con un solo bloque.
# Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el nivel más bajo y devuelva el total 
# de bloques que necesita para construir toda la pirámide

# Declaracion de funcion

def contar_bloques(n):
    if n == 1:
        return 1
    elif n <= 0:
        return print("Error")
    else:
        return n + contar_bloques(n - 1)

# Solicitar valor entrada usuario

n = int(input("Ingrese el numero de bloques en el nivel mas bajo: "))

# Salida al usuario

print(contar_bloques(n))
