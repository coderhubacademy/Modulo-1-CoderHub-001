const productosLocalStorage = JSON.parse(localStorage.getItem("productos"));

const table_body = document.getElementById("main-table-body");

const setElementsTr = (tr, producto) => {
  const td_name = document.createElement("td");
  td_name.innerText = producto.name;
  tr.appendChild(td_name);

  const td_sku = document.createElement("td");
  td_sku.innerText = producto.sku;
  tr.appendChild(td_sku);

  const td_stock = document.createElement("td");
  td_stock.innerText = producto.stock;
  tr.appendChild(td_stock);

  const td_compose_price = document.createElement("td");
  td_compose_price.innerText = producto.compose_price;
  tr.appendChild(td_compose_price);

  const td_single_price = document.createElement("td");
  td_single_price.innerText = producto.single_price;
  tr.appendChild(td_single_price);

  const td_actions = document.createElement("td");
  const select = document.createElement("select");
  select.setAttribute("onchange", "handleSelectChange(this)");
  select.innerHTML = `
    <option value="acciones-${producto.sku}">Acciones</option>
    <option value="editar-${producto.sku}">Editar</option>
    <option value="eliminar-${producto.sku}">Eliminar</option>
  `;
  td_actions.appendChild(select);
  tr.appendChild(td_actions);
};

const handleSelectChange = (select) => {
  const [action, sku] = select.value.split("-");
  const producto = productosLocalStorage.find((p) => p.sku === sku);

  switch (action) {
    case "editar":
      console.log("Editar", producto);
      break;
    case "eliminar":
      console.log("Eliminar", producto);
      break;
    default:
      console.log("Acciones", producto);
      break;
  }
};

productosLocalStorage.forEach((producto) => {
  const tr = document.createElement("tr");
  setElementsTr(tr, producto);
  table_body.appendChild(tr);
});
