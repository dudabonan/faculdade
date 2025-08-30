#include "lista4.h"
#include <stdio.h>

/*
Os elementos devem ser inseridos no início da lista (tal como a Lista 3) e removidos
do início da lista (tal como a Lista 2).
*/

void Inserir_l4(int* lista, int* n, int max, int valor) {
    if (*n >= max) {
        printf("Lista cheia\n");
        return;
    }
    
    for (int i = *n; i > 0; i--) {
        lista[i] = lista[i - 1];
    }
    lista[0] = valor;
    *n += 1;
}

void Remover_l4(int* lista, int* n) {
    if (*n <= 0) {
        printf("Lista vazia\n");
        return;
    }
    
    for (int i = 0; i < *n-1; i++)
        lista[i] = lista[i+1];

    *n -= 1;
}