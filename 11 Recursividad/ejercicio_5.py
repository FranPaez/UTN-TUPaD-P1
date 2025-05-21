# Implementá una función recursiva llamada es_palindromo(palabra) que reciba una cadena de texto sin espacios ni tildes, 
# y devuelva True si es un palíndromo o False si no lo es.
# La solución debe ser recursiva.
# No se debe usar [::-1] ni la función reversed().

# Declaracion de la funcion

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    elif palabra[0] != palabra[-1]:
        return False
    else:
        return es_palindromo(palabra[1:-1])


# Entrada del usuario

palabra = input("Ingrese una palabra: ").lower()

# Salida al usuario

print(es_palindromo(palabra))


