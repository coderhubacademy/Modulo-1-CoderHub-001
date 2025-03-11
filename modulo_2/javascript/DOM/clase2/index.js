const clearForm = () => {
  document.getElementById("nombre").value = "";
  document.getElementById("apellido").value = "";
  document.getElementById("email").value = "";
};

var user_list = [];

const formulario = document.getElementById("primer-formulario");

formulario.addEventListener("submit", (e) => {
  e.preventDefault();

  let nombre = document.getElementById("nombre").value;
  let apellido = document.getElementById("apellido").value;
  let email = document.getElementById("email").value;
  console.log(nombre, apellido, email);
  user_list.push({ nombre, apellido, email });

  let list = document.querySelector("#users");
  let item = document.createElement("li");
  item.innerText = `${nombre} ${apellido} - ${email}`;
  list.appendChild(item);

  console.log("Mi lista", user_list);
  clearForm();
});
