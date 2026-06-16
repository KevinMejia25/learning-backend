#Lista de invitados
# Preguntar cuántos invitados quiere registrar. Guardarlos en una lista. Mostrar la lista numerada.

invitados = []
cuantos = int(input("Cuantos invitados se quieren registrar? "))
for i in range(cuantos):
    nombre = input("Ingrese el nombre del invitado: ")
    invitados.append(nombre)
print("Lista de invitados registrados: ")
contador = 1
for nombre in invitados:
    print(f"{contador}. {nombre}")
    contador += 1
