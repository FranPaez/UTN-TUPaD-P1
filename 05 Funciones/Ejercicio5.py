# Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y devuelva la 
# cantidad de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.

# Declaracion de funciones

def segundos_a_horas(seg):
    return seg / 3600

# Programa principal

segundos = float(input("Ingrese los segundos: "))
horas = segundos_a_horas(segundos)

print(f"{segundos} segundos en horas es: {horas}hs")