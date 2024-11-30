import math
import random
import datetime
import string

# Ejemplos Math

print(math.pi)

print(math.sqrt(25))

def raiz_cuadrada(numero):
  return math.sqrt(numero)

print(raiz_cuadrada(8))

# Ejemplos Random

print(random.randint(1, 100))

def numero_aleatorio():
  return random.randint(1, 100)
  
print(numero_aleatorio())
print(numero_aleatorio())
print(numero_aleatorio())

# Ejemplos con datetime

print(datetime.datetime.now())

print(datetime.datetime.now().year)

print(datetime.datetime.strptime("2021-12-31", "%Y-%m-%d"))

# Ejemplos con string

print(string.ascii_letters)

cadena = "Hola Mundo"
print(cadena.upper())

def is_upper(cadena):
  return cadena.isupper()

print(is_upper("HOLA"))