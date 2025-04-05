const form = document.getElementById("add-form");

form.addEventListener("submit", (e) => {
  e.preventDefault();
  console.log("Aqui");
  console.log("e", e.target);

  const product_name = e.target.name.value;
  console.log("product_name", product_name);
  const single_price = e.target.retail_price.value;
  console.log("single_price", single_price);
  const compose_price = e.target.wholesale_price.value;
  console.log("compose_price", compose_price);
  const sku = e.target.sku.value;
  console.log("sku", sku);
  const stock = e.target.quantity.value;
  console.log("stock", stock);

  const producto = {
    name: e.target.name.value,
    single_price: e.target.retail_price.value,
    compose_price: e.target.wholesale_price.value,
    sku: e.target.sku.value,
    stock: e.target.quantity.value,
  };
  console.log("Producto", producto);
  const productosLocalStorage = JSON.parse(localStorage.getItem("productos"));
  console.log("productos", productosLocalStorage);
  productosLocalStorage.push(producto);
  console.log("productosAct", productosLocalStorage);

  localStorage.setItem("productos", JSON.stringify(productosLocalStorage));
  window.location.href = "./index.html";
});
