// document.body.style.backgroundColor = "red";

let parrafo = document.getElementById("parrafo");
console.log(parrafo);

parrafo.innerText = "Manipulando el dom por primera vez";

let titulo = document.querySelector(".title");
console.log(titulo);

let parrafo2 = document.getElementsByClassName("parrafo2")[0];
console.log(parrafo2);

let lenguajes = document.querySelectorAll("#lenguajes li");

let lenguaje1 = lenguajes[0];

console.log(lenguajes);

var lista_lenguajes = document.getElementById("lenguajes");
console.log(lista_lenguajes);

let nuevo_lenguaje = document.createElement("li");
nuevo_lenguaje.innerText = "c#";

lista_lenguajes.appendChild(nuevo_lenguaje);

document.body.removeChild(parrafo2);

// Eventos

// let boton = document.getElementById("boton");
// boton.addEventListener("click", () => {
//   document.body.style.backgroundColor = "red";
// });

const agregarLenguaje = () => {
  let input = document.getElementById("add-input");
  let nuevo_lenguaje = document.createElement("li");
  nuevo_lenguaje.innerText = input.value;

  lista_lenguajes.appendChild(nuevo_lenguaje);
  input.value = "";
};

const filtrarLenguajes = () => {
  let input = document.getElementById("add-input");
  let value = input.value.toLowerCase();
  let lenguajes = document.querySelectorAll("#lenguajes li");

  lenguajes.forEach((lenguaje) => {
    if (lenguaje.innerText.toLowerCase().includes(value)) {
      lenguaje.style.display = "block";
    } else {
      lenguaje.style.display = "none";
    }
  });
};

let botonAgregar = document.getElementById("add-button");
botonAgregar.addEventListener("click", agregarLenguaje);

let botonFiltrar = document.getElementById("filter-button");
botonFiltrar.addEventListener("click", filtrarLenguajes);
