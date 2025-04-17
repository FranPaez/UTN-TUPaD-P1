# Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es. 
# El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano.

# Declaracion de variables ingresadas por el usuario

hemisferio = input("Indique en que hemisferio se encuentra. N para Norte y S para Sur: ").upper()
mes = input("Indique en que mes se encuentra: ").lower()
dia = int(input("Indique que dia es: "))

# Declaración de variables con los meses para verificar fechas
verificarMesDM = "diciembre enero febrero marzo"
verificarMesMJ = "marzo abril mayo junio"
verificarMesJS = "junio julio agosto septiembre"
verificarMesSD = "septiembre octubre noviembre diciembre"

# Declaracion de condicionales para correcto funcionamiento

if mes in verificarMesDM and hemisferio == "N":
    if ((mes == "diciembre" and dia >= 21) or (mes == "marzo" and dia <= 20)) or (mes == "enero" or mes == "febrero"):
        print("Es Invierno")
if mes in verificarMesMJ:
    if ((mes == "marzo" and dia >= 21) or (mes == "junio" and dia <= 20)) or (mes == "abril" or mes == "mayo"):
        print("Es Primavera")
if mes in verificarMesJS:
    if ((mes == "junio" and dia >= 21) or (mes == "septiembre" and dia <= 20)) or (mes == "julio" or mes == "agosto"):
        print("Es Verano")
if mes in verificarMesSD:
    if ((mes == "septiembre" and dia >= 21) or (mes == "diciembre" and dia <= 20)) or (mes == "octubre" or mes == "noviembre"):
        print("Es Otoño")

if mes in verificarMesDM and hemisferio == "S":
    if ((mes == "diciembre" and dia >= 21) or (mes == "marzo" and dia <= 20)) or (mes == "enero" or mes == "febrero"):
        print("Es Verano")
if mes in verificarMesMJ:
    if ((mes == "marzo" and dia >= 21) or (mes == "junio" and dia <= 20)) or (mes == "abril" or mes == "mayo"):
        print("Es Otoño")
if mes in verificarMesJS:
    if ((mes == "junio" and dia >= 21) or (mes == "septiembre" and dia <= 20)) or (mes == "julio" or mes == "agosto"):
        print("Es Invierno")
if mes in verificarMesSD:
    if ((mes == "septiembre" and dia >= 21) or (mes == "diciembre" and dia <= 20)) or (mes == "octubre" or mes == "noviembre"):
        print("Es Primavera")

