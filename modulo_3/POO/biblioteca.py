class Libro:
  def __init__(self, titulo, autor, anio, code):
    self.titulo = titulo
    self.autor = autor
    self.anio = anio
    self.code = code 
    self.prestado = False
    
  def __str__(self):
    return f"{self.titulo} de {self.autor}, publicado en {self.anio}"
  
class Usuario:
  def __init__(self, nombre, edad):
    self.nombre = nombre
    self.edad = edad
    
  def __str__(self):
    return f"Usuario: {self.nombre}, Edad: {self.edad}"
  
class Bibloteca:
  def __init__(self):
    self.libros = []
    
  def agregar_libro(self, libro):
    if not isinstance(libro, Libro):
      print("El objeto no es una instancia de la clase Libro.")
      return
    if libro == None:
      print("El libro no puede ser None.")
      return
    
    self.libros.append(libro)
    print(f"El libro {libro.titulo} fue agregado a la biblioteca.")
    
  def buscar_libro(self, code):
    for libro in self.libros:
      if libro.code == code:
        return libro
    return None
    
  def prestar_libro(self, code):
    libro = self.buscar_libro(code)
    if libro:
      if libro.prestado:
        print(f"El libro {libro.titulo} ya está prestado.")
      else:
        libro.prestado = True
        print(f"El libro {libro.titulo} ha sido prestado.")
    else:
      print("Libro no encontrado.")
    
    
  def mostrar_libros(self):
    print("Libros en la biblioteca:")
    for libro in self.libros:
      print(libro)

usuario1 = Usuario("Miguel de cervantes", 25)
usuario2 = Usuario("Gabriel Garcia Marquez", 30)


libro1 = Libro("El Quijote", usuario1.nombre, 1605, "123456")
libro2 = Libro("Cien años de soledad", usuario2.nombre, 1967, "654321")

print(libro1)

biblioteca = Bibloteca()
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)

biblioteca.mostrar_libros()

biblioteca.prestar_libro("123456")
biblioteca.prestar_libro("654324")