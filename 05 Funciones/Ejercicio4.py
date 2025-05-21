# Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. 
# calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. 
# Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.

# Declaracion de funciones

pi = 3.14

def calcular_area_circulo(radio):
    return pi * (radio * radio)


def calcular_perimetro_circulo(radio):
    return 2 * pi * radio

# Programa principal

radio_usuario = float(input("Ingrese el radio: "))
area = calcular_area_circulo(radio_usuario)
perimetro = calcular_perimetro_circulo(radio_usuario)

print(f"El área del círculo con radio {radio_usuario} es {area:.2f}")
print(f"El perímetro del círculo con radio {radio_usuario} es {perimetro:.2f}")
