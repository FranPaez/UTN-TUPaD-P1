# Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva un saludo personalizado.
# Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. 
# Llamar a esta función desde el programa principal solicitando el nombre al usuario

# Declaracion de funciones


def saludar_usuario(nombre):
    print(f"Hola {nombre}!")

# Programa principal

nombre_usuario = input("Ingrese su nombre: ")
saludar_usuario(nombre_usuario)

