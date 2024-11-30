# Diferencias Cadenas y Listas
# Listas Anidadas
# Matrices
# Operaciones con Listas


# Las cadenas son inmutables, es decir no se pueden modificar, en cambio 
# las listas si son mutables, es decir se pueden modificar.

# Cadenas
palabra = "Hola"
print(palabra[0])

for letra in palabra:
  print(letra)

# Listas
lista = [1, 2, 3, 4, 5]
print(lista[0])

lista[0] = 10
print("lista", lista)

for numero in lista:
  print(numero)
  
a = 1 

a = a + 1

print("A", a)

# Split - Join

# Split: Nos permite separar una cadena de texto en una lista

# Join: Nos permite unir una lista en una cadena de texto

frase = "Hola como estas"

array_frase = frase.split(" ")

print(frase.split(" "))

array_to_string = " ".join(array_frase)

print(array_to_string)


# Listas Anidadas

notas = [[10, 15, 20], [12, 18, 20], [6, 15, 20]]

print(notas[1])


notas_final = []
for nota in notas:
  notas_final.append(sum(nota) / len(nota))
  
print(notas_final)

# Matrices

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

#matriz[0]
#matriz[1]
#matriz[2]

for fila in matriz:
  for columna in fila:
    print(columna, end="  ")
  print("\n")
