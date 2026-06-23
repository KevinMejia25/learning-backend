#MINI PROYECTO: CALCULADORA DE COMPRAS
 
#Crear funciones que pidan el nombre y el precio, calcular y devolver el total en base a la cantidad del producto


def pedir_producto():
    nombre = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad: "))
    precio = float(input("Ingrese el precio: "))
    return nombre, cantidad, precio
nombre, cantidad, precio = pedir_producto()

def calcular_total(precio, cantidad):
    return precio * cantidad
total = calcular_total(precio, cantidad)

def mostrar_resumen(nombre, total):
    print(f"Producto: {nombre}\nTotal: {total}")
mostrar_resumen(nombre, total)
