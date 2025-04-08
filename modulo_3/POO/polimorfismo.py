class Persona():
    def __init__(self, nombre, apellido, cedula, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.edad = edad
      
    def mostrar_informacion(self):
        print(f"Hola mis datos son, Nombre: {self.nombre}, Apellido: {self.apellido}, Cedula: {self.cedula}, Edad: {self.edad}")
        
class Estudiante(Persona):
    def __init__(self, nombre, apellido, cedula, edad, carrera, notas):
        super().__init__(nombre, apellido, cedula, edad)
        self.carrera = carrera
        self.notas = notas
        
    def horario(self):
        print(f"Hola soy {self.nombre} y estudio {self.carrera} y tengo un horario de clases")
        
class Docente(Persona):
    def __init__(self, nombre, apellido, cedula, edad, asignatura):
        super().__init__(nombre, apellido, cedula, edad)
        self.asignatura = asignatura
    
    def horario(self):
        print(f"Hola soy {self.nombre} y soy docente de {self.asignatura} y tengo un horario de clases")
        
# Polimorfismo: Permite que diferentes clases implementen el mismo método 
# de diferentes maneras

estudiante1 = Estudiante("Juan", "Pérez", "12345678", 20, "Ingeniería", [90, 85, 88])
docente1 = Docente("María", "Gómez", "87654321", 35, "Matemáticas")
estudiante1.mostrar_informacion()
docente1.mostrar_informacion()

print("Mostrando Horarios:", "\n")
def mostrar_horario(persona):
    persona.horario()
    
mostrar_horario(estudiante1)
mostrar_horario(docente1)