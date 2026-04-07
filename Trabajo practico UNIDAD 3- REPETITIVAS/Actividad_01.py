# Ejercicio 1— “Caja del Kiosco”
# Objetivo: Simular una compra con validaciones y cálculo de total.

# VALIDAR NOMBRE
nombre = input("Cliente: ").strip()

while nombre == "" or not nombre.isalpha():
    nombre = input("Error. Ingrese un nombre válido (solo letras): ").strip()

#VALIDAR CANTIDAD DE PRODUCTOS
cantidad = input("Cantidad de productos: ")

while not cantidad.isdigit() or int(cantidad) <= 0:
    cantidad = input("Error. Ingrese una cantidad válida mayor a 0: ")

cantidad = int(cantidad)

#VARIABLES ACUMULADORAS
total_sin_descuento = 0
total_con_descuento = 0

#CARGA DE PRODUCTOS
for i in range(1, cantidad + 1):

    #VALIDAR PRECIO
    precio = input(f"Producto {i} - Precio: ")

    while not precio.isdigit():
        precio = input("Error. Ingrese un precio válido: ")

    precio = int(precio)

    #VALIDAR DESCUENTO
    descuento = input("Descuento (S/N): ").lower()

    while descuento not in ["s", "n"]:
        descuento = input("Error. Ingrese S o N: ").lower()

    #ACUMULAR TOTAL SIN DESCUENTO
    total_sin_descuento += precio

    #APLICAR DESCUENTO SI CORRESPONDE
    if descuento == "s":
        precio_con_desc = precio * 0.9
    else:
        precio_con_desc = precio

    #ACUMULAR TOTAL CON DESCUENTO
    total_con_descuento += precio_con_desc

#CALCULO FINAL
ahorro = total_sin_descuento - total_con_descuento
promedio = total_con_descuento / cantidad

#RESULTADOS
print("\n----- RESUMEN DE COMPRA -----")
print(f"Total sin descuentos: ${total_sin_descuento}")
print(f"Total con descuentos: ${total_con_descuento:.2f}")
print(f"Ahorro: ${ahorro:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")