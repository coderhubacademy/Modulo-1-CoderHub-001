# Explicacion de funciones llamando a otras funciones

def imprimirLinea():
    print("Linea")

def imprimirTresLineas():
  imprimirLinea()
  imprimirLinea()
  imprimirLinea()
    
print("Inicio")
print(imprimirTresLineas())

def pensionMasculina(persona):
  if persona['edad'] >= 65:
    print('Puede pensionarse')
  else:
    print('No puede pensionarse')

def pensionFemenina(persona):
  if persona['edad'] >= 60:
    print('Puede pensionarse')
  else:
    print('No puede pensionarse')

def validarEdadPension(persona):
  if persona['genero'] == 'M':
    pensionMasculina(persona)
  else:
    pensionFemenina(persona)
    
# Recursividad: Una funcion que se llama a si misma

def factorial(n):
  if n == 1:
    return 1
  else:
    return n * factorial(n - 1)
  
def countDown(n):
  if n == 0:
    print('BOOM!')
  else:
    print(n)
    countDown(n - 1)
    
countDown(5)

