cedulas = ["V-12345678", "E-12345678", "J-12345678", "G-12345678", "P-12345678"]

lista_cedulas = open('cedulas.txt', 'w')

for cedula in cedulas:
  lista_cedulas.write(f"{cedula}\n")

lista_cedulas.close()

# Buscar cedula en el archivo
cedula = input("Ingrese la cedula a buscar: ")
lista_cedulas = open('cedulas.txt', 'r')

lista = lista_cedulas.readlines()

for ci in lista:
  if ci == f"{cedula}\n":
    print("Prueba", ci)

lista_cedulas.close()