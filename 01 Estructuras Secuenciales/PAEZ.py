# 1. Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”. 

print("Hola Mundo!")

# 2. Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado. 
# Por ejemplo: si el usuario ingresa “¡Marcos”, el programa debe imprimir por pantalla “Hola Marcos!”. 
# Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla.  

nombre = input("Escriba su nombre: ")
print(f"¡Hola {nombre}!")

# 3. Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por pantalla una oración con los datos ingresados. 
# Por ejemplo: si el usuario ingresa “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30 años y vivo en Argentina”. 
# Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla.

nombre_ejercicio3 = input("Escriba su nombre: ")
apellido = input("Escriba su apellido: ")
edad = input("Escriba su edad: ")
paisResidencia = input("Escriba su país de residencia: ")

print(f"Soy {nombre_ejercicio3} {apellido}, tengo {edad} años y vivo en {paisResidencia}")

# 4. Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro. 

radio = int(input("Escriba el radio del circulo: "))
pi = 3.14
perimetro = 2 * pi * radio
area = pi * (radio * radio)

print(f"El area del circulo de radio {radio} es {area} y su perimetro es {perimetro:.2f}")

# 5. Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale. 

segundos = int(input("Escriba los segundos: "))
minutos = segundos / 60
horas = minutos / 60

print (f"La cantidad de horas que serian {segundos} segundos es: {horas:.2f}hs")

# 6. Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número. 

numeroUsuario = int(input("Escriba unn numero: "))
for i in range(1, 11):
    resultado = numeroUsuario * i
    print(f"{numeroUsuario} X {i} = {resultado}")

# 7. Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos. 

primerNumero = int(input("Ingrese un numero entero distinto del 0: "))
segundoNumero = int(input("Ingrese otro numero distinto de 0: "))
suma = primerNumero + segundoNumero
resta = primerNumero - segundoNumero
multiplicacion = primerNumero * segundoNumero
division = primerNumero / segundoNumero

print(f"Esto es el resultado de realizar diferentes operaciones con los numeros: ")
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")

# 8. Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal. 
# Tener en cuenta que el índice de masa corporal se calcula del siguiente modo: 𝐼𝑀𝐶 = 𝑝𝑒𝑠𝑜 𝑒𝑛 𝑘𝑔 (𝑎𝑙𝑡𝑢𝑟𝑎 𝑒𝑛 𝑚) 2  

peso = float(input("Ingrese su peso en KG: "))
altura = float(input("Ingrese su altura en metros: "))
alturaCuadrado = altura ** 2
imc = peso / alturaCuadrado
print(f"Tu IMC seria {imc:.2f}")

# 9. Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit. 
# Tener en cuenta la siguiente equivalencia: 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡 = 9 5 . 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐶𝑒𝑙𝑠𝑖𝑢𝑠 + 32 

temperaturaCelcius = float(input("Ingrese la temperatura en grados Celcius: "))
temperaturaFahrenheit = (temperaturaCelcius * 9/5) + 32
print(f"La temperatura convertida a Fahrenheit seria: {temperaturaFahrenheit:.2f}")

# 10. Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números

primerNumero_ejercicio10 = float(input("Ingrese el primer numero: "))
segundNumero_ejercicio10 = float(input("Ingrese el segundo numero: "))
tercerNumero_ejercicio10 = float(input("Ingrese el tercer numero: "))
sumaNumeros = primerNumero_ejercicio10 + segundNumero_ejercicio10 + tercerNumero_ejercicio10
promedio = sumaNumeros / 3
print(f"El primedio entre {primerNumero_ejercicio10}, {segundNumero_ejercicio10} y {tercerNumero_ejercicio10} es: {promedio:.2f}")
