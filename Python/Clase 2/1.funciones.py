# Funciones: Son bloques de código que se ejecutan cuando son llamados. 
# Pueden recibir y devolver datos para comunicarse con el resto del programa 
# y son reutilizables.

# Funciones en incluidas en Python

# print()
# input()
# int()
# float()
# str()
# type()

string_var = "Esto es un string, puede tener letras, números y caracteres especiales."
integer_var = 5
float_var = 3.14

def saludar():
  print("Hola, bienvenido a la clase de Python")
  
saludar()

# Estrucutra de una función en python

# 1. def - palabra reservada para definir una función
# 2. nombre de la función - nombre que se le asigna a la función(No debemos repetir el nombre)
# 3. () - paréntesis que pueden recibir argumentos
# 4. : - dos puntos que indican el inicio del bloque de código de la función
# 5. Cuerpo de la función - bloque de código que se ejecuta cuando se llama la función
# (Importate identar el codigo)
# 6. llamada de la función - ejecutar la función. Nombre + paréntesis 

def saludar_mejorada(nombre):
  print("Hola", nombre, "bienvenido a la clase de Python")
  
def imprimir_linea():
  print()
  
def imprimir_tres_lineas():
  imprimir_linea()
  imprimir_linea()
  imprimir_linea()
  
saludar_mejorada("David")
imprimir_linea()
saludar_mejorada("Francisco")
imprimir_linea()
saludar_mejorada("Ruben")
imprimir_tres_lineas()
saludar_mejorada("Rosangela")
imprimir_linea()
saludar_mejorada("Veronika")
imprimir_linea()

print("Hola de nuevo")

# Parametros y argumentos

def sumar(a, b):
  print("El resultado es", (a + b))

sumar(456, 390)

# Funciones con valor de retorno

name = "David"
lastname = "Marin"

def nombre_completo(nombre, apellido):
  return nombre + " " + apellido

resultado_nombre = nombre_completo(name, lastname)

print("Tu nombre completo es", resultado_nombre)

def calcular_notas(nota1, nota2, nota3):
  return (nota1 + nota2 + nota3) / 3

nota_final = calcular_notas(15, 20, 10)

nombre_1 = input("Ingrese su nombre: ")
nombre_2 = input("Ingrese su nombre: ")

apellido_1 = input("Ingrese su apellido: ")
apellido_2 = input("Ingrese su apellido: ")

nota_persona_1_1 = int(input("Ingrese la nota 1: "))
nota_persona_1_2 = int(input("Ingrese la nota 2: "))
nota_persona_1_3 = int(input("Ingrese la nota 3: "))

# nota_persona_2_1 = int(input("Ingrese la nota 1: "))
# nota_persona_2_2 = int(input("Ingrese la nota 2: "))
# nota_persona_2_3 = int(input("Ingrese la nota 3: "))

nota_final_persona_1 = calcular_notas(nota_persona_1_1, nota_persona_1_2, nota_persona_1_3)
# nota_final_persona_2 = calcular_notas(nota_persona_2_1, nota_persona_2_2, nota_persona_2_3)

nombre_completo_1 = nombre_completo(nombre_1, apellido_1)
# nombre_completo_2 = nombre_completo(nombre_2, apellido_2)

print("La nota final de", nombre_completo_1, "es", nota_final_persona_1)
# print("La nota final de", nombre_completo_2, "es", nota_final_persona_2)



