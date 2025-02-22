// Bucles, Ciclos o Loops

// For
// While
// Do While
// For In
// For Of

// For - Para

// i++ == i = i + 1
for (let i = 0; i < 10; i++) {
  console.log(i);
}

for (let i = 10; i > 0; i--) {
  console.log(i);
}

// Arrays

var numeros = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100];

for (let i = 0; i < numeros.length; i++) {
  console.log(numeros[i]);
}

// While - Mientras

var i = 0;

while (i < 10) {
  console.log(i);
  i++;
}

empleados = [
  { nombre: "Juan", director: false },
  { nombre: "Pedro", director: false },
  { nombre: "Maria", director: false },
  { nombre: "Jose", director: true },
  { nombre: "Ana", director: false },
];

var i = 0;
while (true) {
  console.log(empleados[i].nombre);
  if (empleados[i].director) {
    console.log("El director es", empleados[i].nombre);
    break;
  }
  i++;
}

// Do While - Hacer mientras

var i = 0;

do {
  console.log(i);
  i++;
} while (i < 10);

// For In - Para en

var persona = {
  nombre: "Juan",
  apellido: "Perez",
  edad: 30,
};

for (let propiedad in persona) {
  console.log(propiedad, persona[propiedad]);
}

var array = [10, 20, 30, 40, 50];

for (let indice in array) {
  console.log(indice, array[indice]);
}

// fizzbuzz
n = 100;
for (let i = 1; i <= n; i++) {
  if (i % 3 == 0 && i % 5 == 0) {
    console.log("FizzBuzz");
  } else if (i % 3 == 0) {
    console.log("Fizz");
  } else if (i % 5 == 0) {
    console.log("Buzz");
  } else {
    console.log(i);
  }
}

i = 1;
while (i <= n) {
  if (i % 3 == 0 && i % 5 == 0) {
    console.log("FizzBuzz");
  } else if (i % 3 == 0) {
    console.log("Fizz");
  } else if (i % 5 == 0) {
    console.log("Buzz");
  } else {
    console.log(i);
  }
  i++;
}

// Funciones

function suma(a, b) {
  return a + b;
}

function resta(a, b) {
  return a - b;
}

function multiplicacion(a, b) {
  return a * b;
}

console.log(suma(10, 20));
console.log(suma(30, 40));
console.log(suma(50, 60));

a = 10;
b = 20;
c = multiplicacion(a, b);
d = c - a;
console.log(c);
console.log(d);

function fizzBuzz(index, limit) {
  for (let i = index; i <= limit; i++) {
    if (i % 3 == 0 && i % 5 == 0) {
      console.log("FizzBuzz");
    } else if (i % 3 == 0) {
      console.log("Fizz");
    } else if (i % 5 == 0) {
      console.log("Buzz");
    } else {
      console.log(i);
    }
  }
}

fizzBuzz(1, 100);
fizzBuzz(101, 200);
fizzBuzz(201, 300);
fizzBuzz(301, 400);

function imprimirNombre(nombre, apellido) {
  let nombreCompleto = nombre + " " + apellido;
  console.log("Hola", nombreCompleto);
}

imprimirNombre("Juan", "Perez");
console.log(nombreCompleto);

// Estructuras de datos

// Arrays

var numeros = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100];
console.log(numeros);

console.log(numeros[0]);

// Agregar un elemento al final
numeros.push(110);
console.log(numeros);

// Agregar un elemento al principio
numeros.unshift(0);
console.log(numeros);

// Eliminar el ultimo elemento
numeros.pop();

// Eliminar el primer elemento
numeros.shift();

// Eliminar un elemento en una posicion
numeros.splice(3, 2);
console.log(numeros);

// Objetos

var persona = {
  nombre: "Juan",
  apellido: "Perez",
  edad: 30,
  cedula: "123456789",
};

console.log(persona);
console.log(persona.nombre);
console.log(persona.apellido);
console.log(persona.edad);
console.log(persona.cedula);

// Actualizar un valor
persona.nombre = "Pedro";
console.log(persona);

// Agregar un valor
persona.direccion = "Quito";
console.log(persona);

// Eliminar un valor
delete persona.direccion;
console.log(persona);

// Crear un programa que calcule el salario semanal de un empleado basado en las horas trabajadas.
// Si el empleado trabaja mas de 40 horas, todas esas horas seran extras.
// Crear una funcion que reciba el empleado, el pago por hora y el pago por hora extra.
// La funcion debe retornar el empleado actualizado con su pago total.
// El empleado tiene la siguiente estructura:
// {
//   nombre: "Juan",
//   horas: 45,
//   pagoSemanal: 0,
// }

// 1. Crear lista de empleados
// 2. Crear funcion que calcule el salario semanal
// 3. Iterar la lista de empleados y calcular el salario semanal
// 4. Imprimir el salario semanal de cada empleado

var empleados = [
  {
    nombre: "Juan",
    horas: 45,
    pagoSemanal: 0,
  },
  {
    nombre: "Pedro",
    horas: 40,
    pagoSemanal: 0,
  },
  {
    nombre: "Maria",
    horas: 35,
    pagoSemanal: 0,
  },
  {
    nombre: "Jose",
    horas: 50,
    pagoSemanal: 0,
  },
  {
    nombre: "Ana",
    horas: 38,
    pagoSemanal: 0,
  },
];

function calcularSalario(empleado, pagoHora, pagoHoraExtra) {
  if (empleado.horas > 40) {
    empleado.pagoSemanal =
      40 * pagoHora + (empleado.horas - 40) * pagoHoraExtra;
  } else {
    empleado.pagoSemanal = empleado.horas * pagoHora;
  }

  return empleado.pagoSemanal;
}

empleados.forEach((empleado) => {
  console.log(
    empleado.nombre,
    empleado.horas,
    "Salario Semanal",
    calcularSalario(empleado, 10, 15)
  );
});

// for (let i = 0; i < empleados.length; i++)
