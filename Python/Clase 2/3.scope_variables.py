# Existen dos tipos de variables en Python: locales y globales.

# Las variables locales son aquellas que se definen dentro de 
# una función y solo pueden ser utilizadas dentro de la misma función.

# Las variables globales son aquellas que se definen fuera de una función
# y pueden ser utilizadas en cualquier parte del programa. Para poder modificar 
# una variable global dentro de una función, debemos utilizar la palabra reservada global.

a = 5

def sumar(num1, num2):
  global a
  a = num1 + num2
  return a

resultado = sumar(5, 6)

print(resultado)
print(a)

def resta (num1, num2):
  resultado =  num1 - num2
  return resultado

def multiplicacion(num1, num2):
  resultado = num1 * num2
  return resultado

print(resta(7, 6))
print(multiplicacion(5, 6))