# Clase
# Objeto
# Atributos
# Métodos
# Constructor

class Producto():
  def __init__(self, name, price, stock):
    self.name = name
    self.price = price
    self.stock = stock
  
  def show_stock(self):
    print(f"El stock de {self.name} es {self.stock}")
  
producto = Producto("Coca Cola", 1.50, 100)
producto2 = Producto("Pepsi", 1.50, 100)
print(producto.name)
producto.name = "Fanta"
print(producto.price)
print(producto.stock)
producto.show_stock()

print(producto2.name)
print(producto2.price)
print(producto2.stock)

#Pilares de la POO
# - Abstracción
# - Encapsulamiento
# - Herencia
# - Polimorfismo

# Abstracción: Ocultar la complejidad de un sistema y mostrar solo lo necesario
# Encapsulamiento: Proteger los datos y métodos de una clase

# Ejemplo de abstracción y encapsulamiento

class CuentaBancaria():
  def __init__(self, numero, saldo):
    self.numero = numero
    self.__saldo = saldo # Atributo privado
  
  def depositar(self, cantidad):
    self.__saldo += cantidad
  
  def retirar(self, cantidad):
    if cantidad > self.__saldo:
      print("No hay suficiente saldo")
    else:
      self.__saldo -= cantidad
  
  def mostrar_datos(self):
    print(f"Numero de cuenta: {self.numero} y saldo: {self.__saldo}")
  
  def get_metodo_privado(self):
    self.__metodo_privado()

  # metodo privado
  def __metodo_privado(self):
    print("Este es un metodo privado")
    
cuenta = CuentaBancaria("123456789", 1000)
cuenta.mostrar_datos()
cuenta.depositar(500)
cuenta.mostrar_datos()
cuenta.retirar(2000)
cuenta.mostrar_datos()
cuenta.get_metodo_privado()

