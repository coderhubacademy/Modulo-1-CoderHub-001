class Transportista:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return f"Transportista: {self.nombre}"
      
class Carro(Transportista):
    def __init__(self, nombre, marca, modelo):
        super().__init__(nombre)
        self.marca = marca
        self.modelo = modelo
      
    def __str__(self):
        return f"Carro: {self.marca} {self.modelo}, Transportista: {self.nombre}"
    
    def moverse(self):
        return f"{self.nombre} está moviendo el carro {self.marca} {self.modelo}"

class Avion(Transportista):
    def __init__(self, nombre, marca, modelo):
        super().__init__(nombre)
        self.marca = marca
        self.modelo = modelo
      
    def __str__(self):
        return f"Avión: {self.marca} {self.modelo}, Transportista: {self.nombre}"
    
    def moverse(self):
        return f"{self.nombre} está moviendo el avión {self.marca} {self.modelo} por el aire"

class Barco(Transportista):
    def __init__(self, nombre, marca, modelo):
        super().__init__(nombre)
        self.marca = marca
        self.modelo = modelo
      
    def __str__(self):
        return f"Barco: {self.marca} {self.modelo}, Transportista: {self.nombre}"
    
    def moverse(self):
        return f"{self.nombre} está moviendo el barco {self.marca} {self.modelo} por el agua"
      
class ServicioTransporte():
    def __init__(self, transportista):
        self.transportista = transportista
      
    def iniciar_transporte(self):
        return self.transportista.moverse()
        
t1 = Carro("Juan", "Toyota", "Corolla")
t2 = Avion("Pedro", "Boeing", "747")
t3 = Barco("Luis", "Yate", "Xtreme")

print(t1)
print(t2)
print(t3)

servicio1 = ServicioTransporte(t1)
servicio2 = ServicioTransporte(t2)
servicio3 = ServicioTransporte(t3)

print(servicio1.iniciar_transporte())
print(servicio2.iniciar_transporte())
print(servicio3.iniciar_transporte())