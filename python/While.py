#TEMA: WHILE

#¿Que es un while? Mientras esta condición sea verdadera, sigue ejecutando este bloque.

#ejemplo:
contador = 1

while contador <= 5:
    print(contador)
    contador += 1

#Ejercicio 1: cuenta ascendente del 1 al 10
contado = 1
while contado <= 10:
    print(contado)
    contado += 1

#Ejercicio 2: cuenta descendente del 10 al 1
contador = 10
while contador >=1:
    print(contador)
    contador -= 1

#Mini Proyecto: Cajero automático
saldo = 1000
print("Bienvenido al cajero automático")
print("")
opcion = int(input("1. Ver saldo\n2. Depositar dinero\n3. Salir\nSeleccione una opción: "))
while opcion !=3:
    if opcion == 1:
        print(f"Su saldo es: {saldo}")
    elif opcion == 2:
        deposito = int(input("Ingrese la cantidad a depositar: "))
        saldo += deposito
        print(f"Depósito exitoso. Su nuevo saldo es: {saldo}")
    else:
        print("Opción no válida.")
    
    opcion = int(input("1. Ver saldo\n2. Depositar dinero\n3. Salir\nSeleccione una opción: "))
print("Gracias por usar el cajero automático. ¡Hasta luego!")

# += sirve para sumar a una variable y asignar el resultado a esa misma variable. Por ejemplo, saldo += deposito es equivalente a saldo = saldo + deposito.