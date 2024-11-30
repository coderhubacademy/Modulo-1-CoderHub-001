#include <stdio.h>

int mayor_de_edad(int edad) {
    if (edad >= 18) {
        return 1;
    } else {
        return 0;
    }
}

int main() {
    int resultado;
    // int numero = 10;

    // if (numero > 5) {
    //     printf("El número es mayor que 5\n");
    // } else {
    //     printf("El número es menor o igual a 5\n");
    // }

    int edad = 20;
    resultado = mayor_de_edad(edad);

    if (resultado == 1) {
        printf("Eres mayor de edad\n");
    } else {
        printf("Eres menor de edad\n");
    }
    return 0;
}