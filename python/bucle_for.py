#Parte #1 Bucle For

#El for se usa cuando se quiere recorrer una secuencia de elementos, como una lista, tupla, diccionario, conjunto o cadena de texto.

#Ejemplo:
for numero in range(5):
    print(numero)

for numero in range(1, 6):
    print(numero)

#Ejercicio 1: Mostrar los números del 1 al 10 utilizando un bucle for.
for numero in range(1, 11):
    print(numero)

#Ejercicio 2: Mostrar los numeros del 10 al 1 utilizando un bucle for.
for numero in range(10, 0, -1): #El tercer argumento es el paso, en este caso -1 para contar hacia atrás.
    print(numero)

# Parte #2 Listas
#Una lista es una colección ordenada y mutable de elementos. Se pueden agregar, eliminar o modificar elementos en una lista.

#EJemplo:
frutas = ["manzana", "pera", "uva"]
print(frutas)
#Acceder a un elemento de la lista
print(frutas[0]) #Imprime "manzana"
frutas.append("sandia")#Agregar un elemento a la lista
print(frutas)
for fruta in frutas:
    print(fruta)

#Ejercicio 3: Crea una lista
videojuegos = [
    "Minecraft",
    "Valorant",
    "League of Legends",
    "GTA V"
]
for juego in videojuegos:
    print(juego)

#Mini proyecto: Lista de compras gamer
productos = []
for i in range(3): #El rango de 3 es para que el usuario ingrese 3 productos, pero se puede cambiar a cualquier número.
    producto = input("Ingrese un producto para su lista de compras gamer: ")
    productos.append(producto) #Agrega el producto ingresado a la lista de productos.
print("Tu lista de compras gamer es:")
for producto in productos: #Recorre la lista de productos y los imprime uno por uno.
    print(producto)


