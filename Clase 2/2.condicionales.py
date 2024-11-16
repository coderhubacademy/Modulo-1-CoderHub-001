# Condicioales: Son estructuras de control que permiten tomar decisiones en un programa.

# if
# else 
# elif
# switch - case

# def mayor_de_edad(edad):
#   if edad >= 18:
#     print("Eres mayor de edad")
#   else:
#     print("Eres menor de edad")
    
# mayor_de_edad(25)

# numero = 25

# numero_usuario = input("Ingrese un número: ")

# print(type(numero_usuario))
# print(type(numero))

# if numero != numero_usuario:
#   print("No son iguales")
  
def comparador_de_numeros(a, b):
  if type(a) == str or type(b) == str:
    print("Los valores no son números")
  else:
    if a == b:
      print("Los números son iguales")
    else:
      print("Los números no son iguales")
    
comparador_de_numeros(5, 5)

# if, elif, else
# match - case

def comparador_de_numeros_v2(a, b):
  if type(a) == str or type(b) == str:
    print("Los valores no son números")
  elif a == b:
    print("Los números son iguales")
  else:
    print("Los números no son iguales")
    
def dias_por_mes(mes):
  if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    print("El mes tiene 31 días")
  elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    print("El mes tiene 30 días")
  elif mes == 2:
    print("El mes tiene 28 o 29 días")
  else:
    print("El mes no es válido")
    
def dias_mes_v2(nombre_mes):
  print("Variable mes", nombre_mes)
  match nombre_mes:
    case "Enero" | "Marzo" | "Mayo" | "Julio" | "Agosto" | "Octubre" | "Diciembre":
      print("El mes tiene 31 días")
    case "Abril":
      print("El mes tiene 30 días")
    case "Febrero":
      print("El mes tiene 28 o 29 días")
    case _:
      print("El mes no es válido")
      
dias_mes_v2("Marzo")

def edad_pesona_with_match(edad):
  match edad:
    case 0 | 1 | 2 | 3 | 4 | 5:
      print("Eres un bebé")
    case 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17:
      print("Eres un niño")
    case 18 | 19 | 20:
      print("Eres un joven")
    case _:
      print("Eres un adulto")