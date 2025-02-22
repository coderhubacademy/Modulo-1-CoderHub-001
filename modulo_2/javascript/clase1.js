// Valores y tipos de datos
// Variables
// Operadores
// Condicionales
// Bucles
// Funciones
// Scope
// Estrucutras de datos
// Metodos
// Librerias

// Valores y tipos de datos

// Valores primitivos

// String - Cadena de texto - "Hola mundo" o 'Hola mundo'
// Number - Numero - 1234
// Boolean - Valor de verdad - true o false
// Null - Valor nulo - null
// Undefined - Valor indefinido - undefined
// Symbol - Valor simbolico - Symbol('foo')
// BigInt - Valor numerico grande - 9007199254740991n
// NaN - Valor no numerico - NaN

// Variables

// var - Declaracion de variable global
// let - Declaracion de variable local
// const - Declaracion de constante

// Etapas de una variable

// Declaracion
// Inicializacion
// Uso

let word = "Hola mundo";
console.log(word);

var number = 1234;
console.log("Esto es un numero", number);

const pi = 3.1416;
console.log("Esto es una constante", pi);

// Operadores

// Aritmeticos

// Suma - +
// Resta - -
// Multiplicacion - *
// Division - /
// Modulo - %

// Asignacion

// Igual - =
// Suma y asigna - +=
// Resta y asigna - -=
// Multiplica y asigna - *=
// Divide y asigna - /=
// Modulo y asigna - %=
// Incremento - ++
// Decremento - --

// Comparacion

// Igual - ==
// Estrictamente igual - ===
// Diferente - !=
// Estrictamente diferente - !==
// Mayor que - >
// Menor que - <
// Mayor o igual que - >=
// Menor o igual que - <=

// Logicos

// Y - && - and
// O - || - or
// Negacion - ! - not

a = 5;
b = 3;
c = 6;
d = 2;

var suma = a + b;
var resta = a - b;
var multiplicacion = a * c;
var division = c / d;
var modulo = a % d;

console.log("Suma", suma);
console.log("Resta", resta);
console.log("Multiplicacion", multiplicacion);
console.log("Division", division);
console.log("Modulo", modulo);

notas = [10, 20, 40];

nota_final = (notas[0] + notas[1] + notas[2]) / 3;

console.log("Nota final", nota_final);

a += 5;
console.log("Incremento", a);

b -= 2;
console.log("Decremento", b);

console.log("Comparacion", a == b);
console.log("Comparacion estricta", a === b);

console.log("Comparacion", a != b, "A", a, "B", b);

// Condicionales

// if - Si
// else - Si no
// else if - Si no si

var edad = 51;

if (edad >= 18 && edad <= 50) {
  console.log("Eres apto para el trabajo");
} else {
  console.log("No eres apto para el trabajo");
}

mes = 2;

if (mes == 1) {
  console.log("Enero");
} else if (mes == 2) {
  console.log("Febrero");
} else if (mes == 3) {
  console.log("Marzo");
} else {
  console.log("Mes no valido");
}

switch (mes) {
  case 1:
    console.log("Enero - Switch");
    break;
  case 2:
    console.log("Febrero - Switch");
    break;
  case 3:
    console.log("Marzo - Switch");
    break;
  default:
    console.log("Mes no valido - Switch");
    break;
}
