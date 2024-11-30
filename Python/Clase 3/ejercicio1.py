total = 0
while True:
  if total == 0:
    numero = int(input("Introduce un número:"))
  else:
    numero = int(input("Introduce otro número:"))

  if numero == 0:
    break
  else:
    total = total + numero
    
print("La suma de los números es:", total)

num = None
total = 0
while num != 0:
  num = int(input("Introduce un número:"))
  total = total + num

print("El total es:", total)
