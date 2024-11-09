# Condicioales: Son estructuras de control que permiten tomar decisiones en un programa.

# if
# else 
# elif
# switch - case

def mayor_de_edad(edad):
  if edad >= 18:
    print("Eres mayor de edad")
  else:
    print("Eres menor de edad")
    
mayor_de_edad(25)

numero = 25

numero_usuario = input("Ingrese un número: ")

print(type(numero_usuario))
print(type(numero))

if numero != numero_usuario:
  print("No son iguales")
  
def comparador_de_numeros(a, b):
  if type(a) == str or type(b) == str:
    print("Los valores no son números")
  else:
    if a == b:
      print("Los números son iguales")
    else:
      print("Los números no son iguales")
    
comparador_de_numeros(5, 5)