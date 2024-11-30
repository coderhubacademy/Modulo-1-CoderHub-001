personas = [
  { "nombre": "Juan", "edad": 25, "email": "juan@test.com", "telefono": "0987654320" }
]

def agregar_persona(nombre, edad, email, telefono):
    persona = {
        'nombre': nombre,
        'edad': edad,
        'email': email,
        'telefono': telefono
    }
    personas.append(persona)
    
agregar_persona("David", 25, "david@test.com", "0987654321")
agregar_persona("Francisco", 30, "ff@test.com", "0987654322")

print(personas)
print(len(personas))

def buscar_persona(email):
    for persona in personas:
        if persona['email'] == email:
            return persona
    
    return None