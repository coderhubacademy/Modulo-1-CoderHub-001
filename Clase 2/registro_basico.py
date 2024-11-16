print("Opciones del sistema")
print("1. Registro de usuario")
print("2. Buscar usuario")
print("3. Actualizar usuario")
print("4. Eliminar usuario", "\n")

def registro_usuario():
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    edad = int(input("Ingrese su edad: "))
    print("Usuario registrado correctamente", nombre, apellido, edad)

opcion = int(input("Ingrese una opción: "))

match opcion:
    case 1:
        registro_usuario()
    case 2:
        print("Buscar usuario")
    case 3:
        print("Actualizar usuario")
    case 4:
        print("Eliminar usuario")
    case _:
        print("Opción no válida")