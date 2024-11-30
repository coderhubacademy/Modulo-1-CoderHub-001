def sumar(a, b):
  return a + b

def restar(a, b):
  return a - b

def multiplicar(a, b):
  return a * b

def dividir(a, b):
  return a / b

def presentar_resultado(resultado):
  print("El resultado de la operacion es:", resultado)

a = 5
b = 3
c = 10
d = 2
e = 4

# resultado_suma = 
resultado_resta = restar(sumar(a, b), d)
resultado_multiplicacion = multiplicar(resultado_resta, 150)
resultado_division = dividir(resultado_multiplicacion, e)

presentar_resultado(resultado_division)