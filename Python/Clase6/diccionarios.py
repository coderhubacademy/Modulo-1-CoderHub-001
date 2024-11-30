lista_contactos = ["1234", "23456", "34567", "45678", "56789", "67890", "78901", 
                   "89012", "90123", "01234"]

# Diccionarios: Son colecciones de elementos que se encuentran en pares de clave:valor

contactos = {
  "David": "1234",
  "Francisco": "23456",
  "Ruben": "34567",
  "Rosangela": "45678",
  "Veronika": "56789",
  "Luis": "67890"
  }

print(len(contactos))
print(contactos["David"])

# keys() - Nos permite obtener todas las claves del diccionario
# values() - Nos permite obtener todos los valores del diccionario

print(contactos.keys())
print(contactos.values())

print("David" in contactos)

# Agregar un nuevo contacto

contactos["Jose"] = "78901"

print(contactos)

# Eliminar un contacto

del contactos["David"]

print(contactos)

# Modificar un contacto

contactos["Francisco"] = "09876"

print(contactos)

# Iterar un diccionario

for contacto in contactos:
  print(contacto, ":", contactos[contacto])
  
alumnos = [
  {
    "nombre": "Yonmar",
    "edad": 20,
    "curso": "Python",
    "active": True,
    "notas": [10, 15, 20]
  },
  {
    "nombre": "David",
    "edad": 25,
    "curso": "Python",
    "active": False,
    "notas": [15, 20, 10]
  },
  {
    "nombre": "Francisco",
    "edad": 30,
    "curso": "Python",
    "active": True,
    "notas": [15, 20, 10]
  },
  {
    "nombre": "Rosangela",
    "edad": 35,
    "curso": "Python",
    "active": False,
    "notas": [15, 20, 10]
  },
  {
    "nombre": "Veronika",
    "edad": 40,
    "curso": "Python",
    "active": True,
    "notas": [15, 20, 10]
  }
]

print(alumnos[4]["notas"])

for alumno in alumnos:
  message = ""
  if alumno["active"]: 
    message = "Si" 
  else: 
    message ="No"
  if message == "Si":
    print("Nombre:", alumno["nombre"], "Esta activo?", message)