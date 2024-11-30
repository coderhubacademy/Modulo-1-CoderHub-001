"""Una de las caracteráısticas mas potentes de los lenguajes de programación 
es la capacidad de manipular variables. Una variable es un nombre que hace 
referencia a un valor."""

""" Palabras reservadas en Python:

and  continue  else for  import  not  raise
except from  in  or  return  assert  def
break  del  exec  global  is  pass  try
class elif finally if  lambda  print  while
"""

nombre = "Juan"
edad = 25
PI = 3.1416

print(nombre)

apellido = input("Ingrese su apellido: ")

print("Hola", nombre, apellido)

nombre = "Pedro"

print("Hola", nombre, apellido)

# Reglas para nombrar variables

# 1. Los nombres de las variables pueden contener letras, 
# números y guiones bajos.
# 2. Los nombres de las variables no pueden comenzar con un número.
# 3. Los nombres de las variables no pueden contener espacios.
# 4. Los nombres de las variables no pueden contener caracteres especiales.
# 5. Los nombres de las variables no pueden ser palabras reservadas.

# p$ = "Hola"
# 1nombre = "Juan"

# Fases de una variable

# 1. Declaración
# 2. Inicialización
# 3. Utilización

es_par = True
cargo = "Dev Jr"

print("Hola", nombre, apellido, "tu cargo es", cargo)

# Convenciones para nombrar variables

# snake_case - en python se usa para definir variables
# camelCase
# PascalCase
# kebab-case

nombre_completo = nombre + " " + apellido
# nombreCompleto = nombre + " " + apellido

# print - función que imprime en consola
# input - función que recibe un valor del usuario