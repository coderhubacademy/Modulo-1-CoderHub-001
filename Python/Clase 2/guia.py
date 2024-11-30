# Crear una funcion que reciba una variable y retorne un mensaje con el tipo de la variable

def tipo_variable(variable):
  return type(variable)

a = 5
b = "Hola"
c = 5.5
d = True

print(tipo_variable(a))
print(tipo_variable(b))
print(tipo_variable(c))
print(tipo_variable(d))

print(tipo_variable(a) == int)

def suma(a, b):
  if type(a) == int and type(b) == int:
    print("La suma es:", a + b)
  else:
    print("No se puede sumar")

suma(5, 6)
suma(5, "Hola")

# Crea una funcion mayor_numero que reciba 3 numeros y retorne el mayor de ellos

def mayor_numero(a, b, c):
  if a > b and a > c:
    return a
  elif b > a and b > c:
    return b
  else:
    return c