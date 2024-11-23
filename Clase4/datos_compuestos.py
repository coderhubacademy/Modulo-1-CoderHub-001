# Listas -> Arrays
# Diccionarios -> Objetos -> Hash

# Listas: Son colecciones de elementos que pueden ser de diferentes tipos de datos

lista = [3,4,6,10,8]

print(len(lista))

print(lista[3])

notas = [10, 15, 20, 12, 18, 20, 06]

print(len(notas))

i = 0
total_notas = 0
while i < len(notas):
  total_notas += notas[i]
  i += 1 
  
print("El total de notas es", total_notas / len(notas))


# Datos importantes para trabajar con listas/arrays

# 1. Crear una lista, puedo crear una lista vacía o con elementos y debo utilizar 
# corchetes [] para definir la lista

# 2. Acceder a un elemento de la lista, debo utilizar el índice del elemento que quiero
# acceder(Siempre en las listas el primer indice es 0) y debo utilizar corchetes [] 
# para acceder al elemento

# 3. Modificar un elemento de la lista, debo utilizar el índice del elemento que quiero

# 4.  Agregar elemento, usamos el metodo append para agregar al final de la lista un 
# elemento, y lo usamos de la siguiente manera nombre_lista.append(elemento)

# 5. Eliminar elemento, usamos el metodo pop para eliminar un elemento de la lista

frutas = ["Manzana", "Pera", "Banano", "Fresa"]

print(frutas[1])

frutas[1] = "Mango"

print(frutas[1], '\n')

frutas.append("Naranja")

# frutas.pop()
# .pop() nos sirve para eliminar un elemento del array/lista por defecto sino recibe
# parametros es el ultimo elemento, sino debemos pasarle el indice.

print("frutas len", len(frutas))
print("Ultimo elemento del array", frutas[len(frutas) -1])

for fruta in frutas:
  print(fruta)
  
# Cadenas

nombre = "David"

print(nombre[0])
print(len(nombre))
print(nombre[-1])

for letra in nombre:
  print(letra)
  
cedulas = ["V12345", "V56789", "V78907", "V23456", "V11111", "V99897"]

# ci = "V78907"
# cedula = ->
# 1. "V12345"
# 2. "V56789"
# 3. "V78907"
# 4. "V23456"

print(len(cedulas))

print(cedulas[2])

print(cedulas.index("V78907"))

def buscarCi(ci):
  for cedula in cedulas:
    if ci == cedula:
      index = cedulas.index(ci)
      cedulas.pop(index)
      return print("CI Encontrada y borrada", ci)
  
  return print("ci no encontrada")

buscarCi("V78907")

for cedula in cedulas:
  print(cedula)
  
