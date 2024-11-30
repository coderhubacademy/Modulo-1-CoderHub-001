biblioteca = []

def agregar_libro(titulo, autor, anio, editorial, genero, disponible):
    libro = {
        'titulo': titulo,
        'autor': autor,
        'anio': anio,
        'editorial': editorial,
        'genero': genero,
        'disponible': disponible
    }
    biblioteca.append(libro)
    
def buscar_libro(titulo):
    for libro in biblioteca:
        if libro['titulo'] == titulo:
            return libro
    return None
  
def prestar_libro(titulo):
    libro = buscar_libro(titulo)
    if libro is not None:
        if libro['disponible']:
            libro['disponible'] = False
            return True
        else:
            return False
    else:
        return False
      
def devolver_libro(titulo):
    libro = buscar_libro(titulo)
    if libro is not None:
        if not libro['disponible']:
            libro['disponible'] = True
            return True
        else:
            return False
    else:
        return False
      
agregar_libro('Python para todos', 'Yonmar', 2020, 'Python', 'Programacion', True)
agregar_libro('Javascript para todos', 'Jose', 2022, 'Javascript', 'Programacion', True)
agregar_libro('Las 48 leyes del poder', 'Robert Green', 1997, 'No se', 'Tampoco', True)
agregar_libro('El arte de la guerra', 'Sun Tzu', 500, 'No se', 'Tampoco', True)
agregar_libro('La biblia', 'Dios', 0, 'No se', 'Tampoco', True)
agregar_libro('El quijote', 'Cervantes', 1605, 'No se', 'Tampoco', True)
agregar_libro('El principito', 'Antoine de Saint-Exupéry', 1943, 'No se', 'Tampoco', True)

print(len(biblioteca))

print(biblioteca[2]['titulo'])

for libro in biblioteca:
    if libro['genero'] == 'Programacion':
        print(f"Nombre del libro: {libro['titulo']}  autor: {libro['autor']} y año: {libro['anio']}")
        
