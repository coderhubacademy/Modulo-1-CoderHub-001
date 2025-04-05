class Inventario:
  def __init__(self, nombre_tienda):
    self.nombre_tienda = nombre_tienda
    self.productos = []  # Lista para almacenar productos
  
  def agregar_producto(self, producto):
    self.productos.append(producto)
    print(f"Producto {producto.nombre} agregado al inventario.")
    
  def eliminar_producto(self, producto):
    if producto in self.productos:
      self.productos.remove(producto)
      print(f"Producto {producto.nombre} eliminado del inventario.")
    else:
      print(f"Producto {producto.nombre} no encontrado en el inventario.")
  
  def mostrar_inventario(self):
    print(f"Inventario de {self.nombre_tienda}:")
    for producto in self.productos:
      print(f"- {producto.nombre}: {producto.stock} unidades")
    
class Producto:
  def __init__(self, nombre, precio, stock, sku):
    self.nombre = nombre
    self.precio = precio
    self.stock = stock
    self.sku = sku
    
  def mostrar_stock(self):
    print(f"El producto {self.nombre} tiene {self.stock} unidades en stock.")
    
  def mostrar_datos(self):
    print(f"Nombre: {self.nombre}, Precio: {self.precio}, Stock: {self.stock}, SKU: {self.sku}")
    
inventario = Inventario("Tienda de Ejemplo")
producto = Producto("Coca Cola", 1.50, 100, "SKU001")

inventario.agregar_producto(producto)
producto.mostrar_datos()

inventario.mostrar_inventario()

nombre_producto = input("Ingrese el nombre del producto: ")
precio_producto = float(input("Ingrese el precio del producto: "))
stock_producto = int(input("Ingrese el stock del producto: "))
sku_producto = input("Ingrese el SKU del producto: ")
nuevo_producto = Producto(nombre_producto, precio_producto, stock_producto, sku_producto)
inventario.agregar_producto(nuevo_producto)
inventario.mostrar_inventario()