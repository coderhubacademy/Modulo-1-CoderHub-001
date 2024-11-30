## Archivos en python

# Nos permite leer y escribir archivos, para persistir datos

## Abrir un archivo

# open('nombre_archivo', 'modo') -> 'r' -> read, 'w' -> write, 'a' -> append

## Modos de apertura de archivos

# 'r' -> read -> leer
# 'w' -> write -> escribir
# 'a' -> append -> agregar contenido

# 'r+' -> read and write -> leer y escribir
# 'w+' -> write and read -> escribir y leer

## Crear un archivo

# open('nombre_archivo', 'w')

## Leer un archivo

# read() -> lee todo el contenido del archivo

# readline() -> lee una linea del archivo

# readlines() -> lee todas las lineas del archivo

## Escribir en un archivo

# write('contenido')

# Cerrar un archivo

# close()

# message = "Esto es una prueba de escritura en un archivo"
# new_file = open('archivo.txt', 'w')

# new_file.write(message)

# new_file.close()

# # Actualizar un archivo

# new_file = open('archivo.txt', 'a')

# new_file.write("\nEsto es una segunda linea")

# new_file.close()


# asistentes = [
#               "Yonmar Leal", 
#               "Santiago Esteves", 
#               "Joe Castellanos", 
#               "Ruben Rios",
#               "Carlos Chirinos", 
#               "Jorge Blanchard", 
#               "Hernesto Chirinos",
#               "Clairet Alvarez", 
#               "Andrea Petit", 
#               "Daniela Valbuena",
#               "Rosangela Granda"
#               ]

# lista_asistencia = open('lista.txt', 'w')

# for asistente in asistentes:
#   lista_asistencia.write(asistente)
#   lista_asistencia.write('\n')
  
# lista_asistencia.close()

# Leer archivo

lista_asistencia = open('lista.txt', 'r')

lista_n = lista_asistencia.readlines()
print(lista_n)
for nombre in lista_n:
  if nombre == "Yonmar Leal\n":
    print(nombre)

lista_asistencia.close()