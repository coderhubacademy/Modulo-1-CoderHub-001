from db import create_connection
from models.product import Product
from models.order import Order

connection = create_connection()
cursor = connection.cursor()

while True:
    print ("Bienvenido al sistema de gestion de northwind")
    print()
  
    print("1. Seccion de Productos")
    print("2. Seccion de Ordenes")
    print("3. Seccion de Proveedores")
    print("4. Seccion de Curiers")
    print("5. Salir")
    
    opt = input("Seleccione una opcion: ")
    
    match opt:
        case "1":
            print("Seccion de Productos")
            print("1. Crear Producto")
            print("2. Mostrar Productos")
            print("3. Actualizar Producto")
            print("4. Eliminar Producto")
            print("5. Buscar Producto por Nombre")
            print("6. Salir")
            
            opt = input("Seleccione una opcion: ")
            print()
            
            match opt:
                case "1":
                    print("Crear Producto")
                    print()
                    name = input("Ingrese el nombre del producto: ")
                    price = float(input("Ingrese el precio del producto: "))
                    supplierId = int(input("Ingrese el ID del proveedor: "))
                    categoryId = int(input("Ingrese el ID de la categoria: "))
                    unit = input("Ingrese la unidad del producto: ")
                    
                    product = Product(name, price, supplierId, categoryId, unit)
                    product.create_product(connection)
                case "2":
                    print("Mostrar Productos")
                    # product = Product("", 0, 0, 0, "")
                    Product.list_all(cursor)              
                case "3":
                  print("Actualizar Producto")
                  product_name = input("Ingrese el nombre del producto a actualizar: ")
                  product = Product.find_by_name(cursor, product_name)
                  if product:
                    print("Producto encontrado:", product)
                    new_name = input("Ingrese el nuevo nombre del producto: ")
                    new_price = float(input("Ingrese el nuevo precio del producto: "))
                    new_supplierId = int(input("Ingrese el nuevo ID del proveedor: "))
                    new_categoryId = int(input("Ingrese el nuevo ID de la categoria: "))
                    new_unit = input("Ingrese la nueva unidad del producto: ")
                    product = Product(new_name, new_price, new_supplierId, new_categoryId, new_unit)
                    product.update_product(connection)
                  else:
                    print("Producto no encontrado")
                case "4":
                  print("Eliminar Producto")
                  product_name = input("Ingrese el nombre del producto a eliminar: ")
                  product = Product.find_by_name(cursor, product_name)
                  if product:
                    productID = product[0]
                    cursor.execute("DELETE FROM products WHERE ProductID = ?", (productID,))
                    connection.commit()
                    print(f"Producto {product_name} eliminado con exito")
                  else:
                    print("Producto no encontrado")
                case "5":
                  print("Buscar Producto por Nombre")
                  product_name = input("Ingrese el nombre del producto a buscar: ")
                  product = Product.find_by_name(cursor, product_name)
                  print(product)
                case "6":
                  break
                case _:
                  print("Opcion no valida")
        case "2":
            print("Seccion de Ordenes")
            print("1. Crear Orden")
            print("2. Mostrar Ordenes")
            print("3. Actualizar Orden")
            print("4. Eliminar Orden")
            
            opt = input("Seleccione una opcion: ")
            
            match opt:
                case "1":
                    print("Crear Orden")
                case "2":
                    print("Mostrar Ordenes")                
                case "3":
                  print("Actualizar Orden")
                case "4":
                  print("Eliminar Orden")
                case _:
                  print("Opcion no valida")
        case "3":
            print("Seccion de Proveedores")
            print("1. Crear Proveedor")
            print("2. Mostrar Proveedores")
            print("3. Actualizar Proveedor")
            print("4. Eliminar Proveedor")
            
            opt = input("Seleccione una opcion: ")
            
            match opt:
                case "1":
                    print("Crear Proveedor")
                case "2":
                    print("Mostrar Proveedores")                
                case "3":
                  print("Actualizar Proveedor")
                case "4":
                  print("Eliminar Proveedor")
                case _:
                  print("Opcion no valida")
        case "4":
            print("Seccion de Curiers")
            print("1. Crear Curier")
            print("2. Mostrar Curiers")
            print("3. Actualizar Curier")
            print("4. Eliminar Curier")
            
            opt = input("Seleccione una opcion: ")
            
            match opt:
                case "1":
                    print("Crear Curier")
                case "2":
                    print("Mostrar Curiers")          
                case "3":
                  print("Actualizar Curier")
                case "4":
                  print("Eliminar Curier")
                case _:
                  print("Opcion no valida")
        case "5":
            print("Saliendo del sistema")
            connection.close()
            print("Gracias por usar el sistema de gestion de northwind")
            break
        case _:
            print("Opcion no valida")
            