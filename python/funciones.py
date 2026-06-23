#QUE ES UNA FUNCION
#una función es un bloque de código al que le das un nombre para poder reutilizarlo.

#Ejemplo
def saludar():
    print("Hola")

saludar()

#Ejercicio 1: Crear una funcion que imprima el nombre
def mostrar_nombre():
    nombre = input("Cual es tu nombre? ")
    print(nombre)
mostrar_nombre()

#FUNCIONES CON PARAMETROS: Las funciones pueden recibir informacion
def saludar2(nombre):
    print(f"Hola {nombre}")

saludar2("kevin")

#Ejercicio 2: Crear una funcion que muestre la edad y llamarla
def mostrar_edad():
    edad = int(input("Cual es tu edad? "))
    print(f"Tu edad es: {edad}")
mostrar_edad()

#FUNCIONES CON VARIOS PARAMETROS
def sumar(a, b):
    print(a + b)
sumar(10,5)

#Ejercicio 3: Crear una funcion que muestre el total del precio multiplicado por la cantidad
def multiplicacion(a, b):
    print(f"Total: {a * b}")
multiplicacion(10,5)

#RETURN: Se usa para se quiere que las funciones devualvan un valor
#Ejemplo:
def sumar(a, b):
    return a + b
resultado = sumar(10, 5)
print(resultado)
