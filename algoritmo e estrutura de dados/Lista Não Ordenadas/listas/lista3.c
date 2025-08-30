#include "lista3.h"
#include <stdio.h>

/*
Os elementos devem ser inseridos no início da lista. As remoções devem ser realizadas
de trás para frente, isto é, o último deverá ser o primeiro elemento removido.
*/

void Inserir_l3(int* lista, int* n, int max, int valor) {
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

void Remover_l3(int* lista, int* n) {
    if (*n <= 0) {
        printf("Lista vazia\n");
        return;
    }

    *n -= 1;
}