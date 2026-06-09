#Crea un programa que pregunte: Tu nombre, Cuánto dinero tienes, Cuánto cuesta una GPU, Cuánto cuesta un monitor, Cuánto cuesta un teclado

print("Bienvenido al programa de presupuesto gamer")
nombre = input("Cual es tu nombre? ")
presupuesto = int(input("Cuanto dinero tienes? "))
gpu = int(input("Cuanto cuesta una GPU? "))
monitor = int(input("Cuanto cuesta un monitor? "))
teclado = int(input("Cuanto cuesta un teclado? "))
total = gpu+monitor+teclado
restante = presupuesto - total

print("")
print("Hola", nombre)
print("")
print("Presupuesto inicial de:", presupuesto)
print("")
print("GPU:", gpu)
print("Monitor:", monitor)
print("Teclado:", teclado)
print("")
print("Total de dinero gastado:", total)
if restante>=0:
    print("Dinero restante:", restante)
    print("Puedes comprar todo")
else:
    print("No puedes comprar todo")
    print("Te faltan: ",restante*(-1))


