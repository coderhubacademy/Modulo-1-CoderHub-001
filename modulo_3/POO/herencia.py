# Herencia: Permite crear una nueva clase a partir de una clase existente

class Animal():
  def __init__(self, nombre, patas, color, edad):
    self.nombre = nombre
    self.patas = patas
    self.color = color
    self.edad = edad
  
  def hablar(self):
    print(f"{self.nombre} hace ruido")
  
  def moverse(self):
    print(f"{self.nombre} se mueve")
    
animal1 = Animal("Perro", 4, "Marrón", 5)
animal1.hablar()
    
class Perro(Animal):
  def __init__(self, nombre, patas, color, edad, raza):
    super().__init__(nombre, patas, color, edad)
    self.raza = raza
  
  def hablar(self):
    print(f"{self.nombre} ladra")
  
  def moverse(self):
    print(f"{self.nombre} corre")
    
perro1 = Perro("Firulais", 4, "Marrón", 5, "Labrador")
perro1.hablar()
perro1.moverse()

#Herencia multiple

class Ave():
  def __init__(self, nombre, patas, color, edad):
    self.nombre = nombre
    self.patas = patas
    self.color = color
    self.edad = edad
  
  def hablar(self):
    print(f"{self.nombre} hace ruido")
  
  def moverse(self):
    print(f"{self.nombre} vuela")
    
class Aguila(Ave, Animal):
  def __init__(self, nombre, patas, color, edad):
    super().__init__(nombre, patas, color, edad)
  
  def hablar(self):
    print(f"{self.nombre} grita")
    
  # def moverse(self):
  #   print(f"{self.nombre} vuela alto")
    
aguila1 = Aguila("Aguila", 2, "Marrón", 5)
aguila1.hablar()
aguila1.moverse()

#MRO - Method Resolution Order