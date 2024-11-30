# def numeros_del_1_al_10():
#   print("1")
#   print("2")
#   print("3")
#   print("4")
#   print("5")
#   print("6")
#   print("7")
#   print("8")
#   print("9")
#   print("10")

# numeros_del_1_al_10()

# print("\n", "--------", "\n")

# # While y for

# # lopps - ciclos: Son estructuras de control que repiten un bloque de código

# # while: Mientras la condición sea verdadera, se ejecuta el bloque de código

# # for: Se utiliza para recorrer una secuencia de elementos

# n = 0
# while(n <= 10):
#   print(n)
#   n += 0.5

# print("\n", "--------", "\n")

# for numero in range(1, 11):
#   print(numero)

# def fizz_buzz(numero):
#   if numero % 2 == 0:
#     print(numero, "---", "Fizz")
#   else:
#     print(numero, "---","Buzz")
  
# for numero in range(1, 101):
#   fizz_buzz(numero)

i = 1
while i <= 100:
  i *= 2
  print(i)
  # i += 1
  # i = i + 1, i++
  
def count_down(numero):
  while numero >= 0:
    if numero == 0:
      print("Despegue")
    else:
      print(numero)
    numero -= 1
    
count_down(3)


for letra in "Hola":
  print(letra)
  
numeros = [1,2,3,4,5,6,7,8,9,10]

for numero in numeros:
  print(numero)