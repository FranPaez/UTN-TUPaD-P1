# Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y devuelva su 
# equivalente en Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.

# Declaracion de funciones

def celsius_a_fahrenheit(celcius):
    return (celcius * 9/5) + 32

# Programa principal

celsius = int(input("Ingrese la temperatura en grados Celcius: "))
fahrenheit = celsius_a_fahrenheit(celsius)

print(f"{celsius} grados Celcius equivale a {fahrenheit} grados Fahrenheit")
