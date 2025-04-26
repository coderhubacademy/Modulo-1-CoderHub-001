class Product():
    def __init__(self, name, price, supplierId, categoryId, unit):
      self.name = name
      self.price = price
      self.supplierId = supplierId
      self.categoryId = categoryId
      self.unit = unit

    def __str__(self):
      return f"Product(name={self.name}, price={self.price}, supplierId={self.supplierId}, categoryId={self.categoryId}, unit={self.unit})"
    
    def create_product(self, conn):
      cursor = conn.cursor()
      cursor.execute("INSERT INTO products (ProductName, Price, SupplierID, CategoryID, Unit) VALUES (?, ?, ?, ?, ?)", 
                     (self.name, self.price, self.supplierId, self.categoryId, self.unit))
      conn.commit()
      print(f"Producto {self.name} creado con exito")
    
    def update_product(self, conn):
      cursor = conn.cursor()
      cursor.execute('''
                     UPDATE products SET ProductName = ?, Price = ?, SupplierID = ?, CategoryID = ?, Unit = ? 
                     WHERE ProductName = ?
                     ''', 
                      (self.name, self.price, self.supplierId, self.categoryId, self.unit, self.name)
                     )
      conn.commit()
      print(f"Producto {self.name} actualizado con exito")
    
    @classmethod
    def list_all(cls, cursor):
      cursor.execute("SELECT * FROM products")
      rows = cursor.fetchall()
      for row in rows:
          print(row)
          
    @classmethod
    def find_by_name(cls, cursor, name):
      cursor.execute("SELECT * FROM products WHERE ProductName = ? LIMIT 1", (name,))
      row = cursor.fetchone()
      if row:
          return row
      else:
          print(f"No se encontraron productos con el nombre {name}")