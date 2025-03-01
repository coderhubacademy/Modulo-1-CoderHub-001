// 1. Arrow functions

// Son una forma mas corta de escribir funciones en JavaScript. Se introdujeron en ECMAScript 6.

// Sintaxis

// (param1, param2, ..., paramN) => { sentencias }

function suma(a, b) {
  a + b;
}

function fullName(name, lastname) {
  return name + " " + lastname;
}

function saludar(name) {
  console.log("Hola " + name);
}

var completeName = fullName("Juan", "Perez");

saludar(completeName);

// Arrow functions

var suma = (a, b) => a + b;

console.log(suma(5, 3));

var saludar = (name) => console.log("Hola " + name);

var fullName2 = (name, lastname) => `${name} ${lastname}`;

saludar(fullName2("Juan", "Perez"));

// 2. Programcion funcional y imperativa

// Programacion funcional

// Es un paradigma de programacion que trata de evitar el cambio de estado y los datos mutables. En su lugar, se basa en la evaluacion de funciones matematicas y en la aplicacion de funciones puras.

// Caracteristicas

// - Funciones puras
// - Funciones de primera clase
// - Funciones Callback
// - Funciones de orden superior
// - Funciones recursivas
// - Inmutabilidad

// Programacion imperativa

// Es un paradigma de programacion que se basa en la ejecucion de instrucciones que cambian el estado del programa. Se enfoca en como se deben hacer las cosas.

// Caracteristicas

// - Variables mutables
// - Ciclos
// - Condiciones
// - Estructuras de control
// - Procedimientos
// - Metodos

// Ejemplo funciones puras

const sum = (a, b) => a + b;

console.log(sum(5, 6));

// Fubcion impura

var notaFinal = 0;
const calcularNotaFinal = (nota1, nota2, nota3) => {
  notaFinal += nota1 + nota2 + nota3;
  return notaFinal;
};

console.log(calcularNotaFinal(15, 14, 13));
console.log(calcularNotaFinal(13, 14, 15));

// Ejemplo funciones de primera clase

const hola = (name) => console.log(`Hola ${name}`);

hola("Juan");

// Ejemplo de funciones callback

const sumar = (a, b, callback) => {
  let result = a + b;
  callback(result);
};

sumar(5, 3, (result) => console.log(result));

// Ejemplo de funciones de orden superior

const sumar2 = (a, b) => a + b;

const restar = (a, b) => a - b;

const multiplicar = (a, b) => a * b;

const operacion = (a, b, funcion) => funcion(a, b);

console.log(operacion(15, 30, sumar2));
console.log(operacion(50, 3, restar));
console.log(operacion(5, 6, multiplicar));

var array = [1, 3, 5, "hola", "mundo", 10, 20, 30, false, 17, true];

function filtroArray(array, callback) {
  let newArray = [];
  for (let i = 0; i < array.length; i++) {
    if (callback(array[i])) {
      newArray.push(array[i]);
    }
  }
  return newArray;
}

const filtrarNumeros = filtroArray(
  array,
  (element) => typeof element === "number"
);

// Metodo filter

const filtrarNumeros2 = array.filter((element) => typeof element === "number");

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

for (let i = 0; i < numeros.length; i++) {
  console.log(numeros[i]);
}

// Metodo forEach

numeros.forEach((numero) => console.log(numero));

productos = [
  { nombre: "Play 5", precio: 500, categoria: "Juegos" },
  { nombre: "Xbox", precio: 300, categoria: "Juegos" },
  { nombre: "Nintendo", precio: 250, categoria: "Juegos" },
  { nombre: "Iphone", precio: 1400, categoria: "Celulares" },
  { nombre: "Samsung", precio: 500, categoria: "Celulares" },
  { nombre: "Macbook", precio: 3600, categoria: "Computadoras" },
  { nombre: "Dell", precio: 700, categoria: "Computadoras" },
];

var juegos = [];
var celulares = [];
var computadoras = [];

for (let i = 0; i < productos.length; i++) {
  if (productos[i].categoria === "Juegos") {
    juegos.push(productos[i]);
  } else if (productos[i].categoria === "Celulares") {
    celulares.push(productos[i]);
  } else {
    computadoras.push(productos[i]);
  }
}

var juegos = productos.filter((producto) => producto.categoria === "Juegos");

// Metodo map

var precios = productos.map((producto) => [
  producto.precio + producto.precio * 0.16,
  producto.nombre,
]);

// total = 0;
// precios.forEach((precio) => (total += precio[0]));

// Metodo reduce

var total = precios.reduce((acumulador, precio) => acumulador + precio[0], 0);

console.log(precios);
console.log(total);

// Metodo find

var producto = productos.find((producto) => producto.nombre === "Macbook");

var estudiantes = [
  { nombre: "Juan", ci: "123", edad: 20 },
  { nombre: "Pedro", ci: "456", edad: 25 },
  { nombre: "Maria", ci: "789", edad: 30 },
  { nombre: "Ana", ci: "101", edad: 35 },
];

const buscarEstudiante = (array, ci) => {
  return array.find((estudiante) => estudiante.ci === ci);
};

console.log(buscarEstudiante(estudiantes, "789"));

// Metodo some - retorna un valor booleano

estudiantes.some((estudiante) => estudiante.edad > 30);

// Metodo every - retorna un valor booleano

estudiantes.every((estudiante) => estudiante.edad > 18);
