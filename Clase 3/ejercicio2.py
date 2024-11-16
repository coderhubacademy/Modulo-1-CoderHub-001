# Contar Letras: Pide al usuario que introduzca una frase y utiliza un bucle 
# for para contar cuántas letras hay en la frase (considera a, e, i, o, u).

def contar_letras(frase):
  contador = 0
  for letra in frase:
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
      contador += 1
  return contador

frase = input("Ingrese una frase: ")
print("La frase tiene", contar_letras(frase), "vocales")

