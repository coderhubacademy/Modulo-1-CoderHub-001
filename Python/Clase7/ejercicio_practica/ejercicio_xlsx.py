import openpyxl

estudiantes = []

def mostrar_options():
    print("1. Agregar un estudiante")
    print("2. Buscar un estudiante por cedula")
    print("3. Eliminar un estudiante por cedula")
    print("4. Modificar un estudiante por cedula")
    print("5. Mostrar todos los estudiantes")
    print("6. Agregar notas por excel")
    print("7. Salir")
    print()

def agregar_estudiante():
    cedula = input("Ingrese la cedula del estudiante: ")
    nombre = input("Ingrese el nombre del estudiante: ")
    edad = int(input("Ingrese la edad del estudiante: "))
    carrera = input("Ingrese la carrera del estudiante: ")
    
    estudiante = {
        'cedula': cedula,
        'nombre': nombre,
        'edad': edad,
        'carrera': carrera,
        'notas': []
    }
    
    estudiantes.append(estudiante)

def buscar_estudiante():
    cedula = input("Ingrese la cedula del estudiante: ")
    
    for estudiante in estudiantes:
        if estudiante['cedula'] == cedula:
            print(estudiante, "\n")
            return
    print("Estudiante no encontrado")
    print()
    
def mostrar_estudiantes():
    for estudiante in estudiantes:
        print(f"Nombre: {estudiante['nombre']}, cedula: {estudiante['cedula']}")
    print()

def agregar_notas_excel():
    archivo = input("Ingrese el nombre del archivo: ")
    wb = openpyxl.load_workbook(archivo)
    hoja = wb.active
    
    for fila in hoja.iter_rows(values_only=True):
        cedula = str(fila[0])
        nota1 = fila[1]
        nota2 = fila[2]
        nota3 = fila[3]
        notas = [nota1, nota2, nota3]
        
        print(cedula, notas)
        for estudiante in estudiantes:
            if estudiante['cedula'] == cedula:
                estudiante['notas'] = [nota1, nota2, nota3]
                print("Estudiante", estudiante)
                break
    print("Notas agregadas correctamente")
    print()
  
while True:
    mostrar_options()
    opcion = int(input("Ingrese una opcion: "))
    
    match opcion:
      case 1:
          print("Agregando un estudiante", "\n")
          agregar_estudiante()
      case 2:
          print("Buscar un estudiante por cedula", "\n")
          buscar_estudiante()
      case 3:
          print("Eliminar un estudiante por cedula")
      case 4:
          print("Modificar un estudiante por cedula")
      case 5:
          print("Mostrando todos los estudiantes", "\n")
          mostrar_estudiantes()
      case 6:
          print("Agregar notas por excel", "\n")
          agregar_notas_excel()
      case 7:
          print("Salir")
          break
      case _:
          print("Opcion invalida")
          
    print()