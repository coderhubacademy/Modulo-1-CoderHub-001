def palindromo_david(word):
  reverse_word = list(reversed(word))
  return print(word == ("").join(reverse_word))

palabra = "reconocer"

# def palindromo_santiago(palabra):
#     if palabra == (palabra[::-1]):
#         print("la palabra es palindromo")
#     else:
#         print("la palabra no es palindromo")
        




# def palindromo_ana(palabra):
#     arreglo= []
#     for letra in palabra:
#         arreglo.append(letra)
#     arreglo_alreves= list(reversed(arreglo))
#     if arreglo == arreglo_alreves:
#         print("es palindromo")
#     else:
#         print("no es palindromo")

# palindromo("ana")







# "Hola"

# 4 - letras

# len(hola) -> 4

# 3

# "hola"[3]
def palindromo2(word):
  i = len(word) - 1
  j = 0
  palindromn = True
  
  while i >= 0:
    while j < len(word):
      print("I", word[i])
      print("J", word[j])
      if word[i] != word[j]:
        palindromn = False
      j += 1
      i -= 1
  
  if palindromn == True:
    print("Es palidromo")
  else:
    print("No es palindromo")

    
    
palindromo2("osoi")