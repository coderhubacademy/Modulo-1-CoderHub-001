productos = [
  { nombre: "Macbook", stock: 10 },
  { nombre: "Iphone", stock: 1 },
  { nombre: "Samsung", stock: 5 },
  { nombre: "Dell", stock: 20 },
];

function comprar(nombreProducto, cantidad) {
  let producto = productos.find(
    (producto) => producto.nombre === nombreProducto
  );
  if (producto.stock >= cantidad) {
    producto.stock -= cantidad;
    console.log("Compra exitosa");
  } else {
    console.log("No hay stock suficiente");
  }
}

comprar("Macbook", 10);
comprar("Macbook", 1);
