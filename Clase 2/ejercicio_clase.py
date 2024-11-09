# Pide al usuario que ingrese el total de una cuenta a pagar y la propina, Luego indicar
# Si la propina es mayor a 10 crear un mensaje que diga "Es una propina generosa" o si es menor a 10
# crear un mensaje que diga "Es una propina mala"

def calcular_propina(total_gasto, propina):
  return total_gasto * propina / 100

def validar_propina(propina):
  if propina_calculada > 10:
    print("Es una propina generosa", propina)
  else:
    print("Es una propina mala", propina)

total_gasto = float(input("Ingrese el total de la cuenta a pagar: "))
propina = float(input("Ingrese el total de la propina: "))
propina_calculada = calcular_propina(total_gasto, propina)

validar_propina(propina_calculada)

# Otra forma de hacerlo

# total_gasto = float(input("Ingrese el total de la cuenta a pagar: "))
# propina = float(input("Ingrese el total de la propina: "))
# calculo = total_gasto * propina / 100

# if calculo > 10:
#   print("Es una propina generosa", calculo)
# else:
#   print("Es una propina mala", calculo)