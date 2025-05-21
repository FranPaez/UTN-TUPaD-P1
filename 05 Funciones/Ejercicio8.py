# Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, y devuelva 
# el índice de masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.

# Declaracion de funciones

def calcular_imc(peso, altura):
    alturaCuadrado = altura ** 2
    return peso / alturaCuadrado

# Programa principal
peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))
imc = calcular_imc(peso, altura)

print(f"El IMC para una persona con peso de {peso} kg y altura de {altura} m es: {imc:.2f}")
