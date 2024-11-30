#include <stdio.h>

int suma(int a, int b) {
    int resultado = a + b;
    printf("La suma de %d y %d es %d\n", a, b, resultado);
    return resultado;
}

void saludar(char nombre[]) {
  printf("Hola, %s!\n", nombre);
}

// char nombre_completo(char nombre[], char apellido[]) {
//   char nombre_completo[50];
  
//   char nombre1[50] = "Hola";
//   char nombre2[50] = "Mundo";

//   printf("Tu nombre completo es: %s %s\n", nombre1, nombre2);
// }

int main() {
  char nombre;
  char apellido;
  suma(5, 10);

  // printf("Ingresa tu nombre: ");
  // scanf("%s", nombre);
  // printf("Ingresa tu apellido: ");
  // scanf("%s", apellido);

  saludar(nombre);
  nombre_completo(nombre, apellido);
  return 0;
}

/*

Esto es un comentario multilinea

*/