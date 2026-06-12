# comparaciones-operadores_logicos

# Comparaciones

edad = 20

print(edad > 18) # > es mayor que
print(edad < 18) # < es menor que
print(edad == 20) # == es igual a
print(edad != 20) # != es diferente a



# Operadores lógicos
edad = 20
dinero = 1000

print(edad >= 18 and dinero >= 500) # and es un operador lógico que devuelve True si ambas condiciones son verdaderas



edad = 16
permiso = True
print(edad >= 18 or permiso) # or es un operador lógico que devuelve True si al menos una de las condiciones es verdadera



activo = True
print(not activo) # not es un operador lógico que invierte el valor de verdad

# Ejercicio 1
edad = int(input("¿Cuál es tu edad? "))
if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")

# Ejercicio 2
user = input("Ingrese su nombre de usuario: ")
password = input("Ingrese su contraseña: ")
if user == "admin" and password == "1234":
    print("Acceso concedido.")
else:
    print("Acceso denegado.")


## Mini proyetco: Sistema de acceso a tienda gamer

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
dinero = float(input("Ingrese la cantidad de dinero que tiene: "))
if edad >= 18 and dinero >= 5000:
    print(f"Bienvenido {nombre}, puedes comprar cualquier producto.")
elif edad >= 18 and dinero < 5000:
    print(f"Bienvenido {nombre}, puedes comprar productos de hasta {dinero} pesos")
elif edad < 18:
    print(f"Lo siento {nombre}, necesitas la supervisión de un adulto.")
