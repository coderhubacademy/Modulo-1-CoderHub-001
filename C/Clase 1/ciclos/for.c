#include <stdio.h>

int main() {
    int i;
    for (i = 1; i < 10; i = i * 2) {
        printf("El valor de i es: %d\n", i);
    }
    return 0;
}