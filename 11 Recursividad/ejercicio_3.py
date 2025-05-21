# Crea una función recursiva que calcule la potencia de un número base elevado a un exponente, utilizando la fórmula 
# 𝑛 𝑚 = 𝑛 ∗ 𝑛 (𝑚−1). Prueba esta función en un algoritmo general.

# Declaracion de funcion

def potencia(n, m):
    if m == 0:
        return 1
    else: 
        return n * potencia(n, m - 1)


# Solicitud de entrada al usuario

n = int(input("Ingrese el numero base: "))
m = int(input("Ingrese el exponente al cual elevar el numero base: "))

# Ciclo para que el print funcione correctamente 

print(f"{n} elevado a la {m} es: {potencia(n, m)}")


