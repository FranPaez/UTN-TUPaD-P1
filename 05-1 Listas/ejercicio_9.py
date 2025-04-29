# Dada la lista “compras”, cuyos elementos representan los productos comprados por diferentes clientes:
# Agregar "jugo" a la lista del tercer cliente usando append.
# Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
# Eliminar "pan" de la lista del primer cliente.
# Imprimir la lista resultante por pantalla
# compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

cliente_1 = ["pan", "leche"]
cliente_2 = ["arroz", "fideos", "salsa"]
cliente_3 = ["agua"]

cliente_3.append("jugo")
cliente_2[1] = "tallarines"
cliente_1.remove("pan")

compras = cliente_1 + cliente_2 + cliente_3
print(compras)