#include "lista1.h"
#include <stdio.h>

/*
Os elementos devem ser inseridos no final da lista. As remoções devem ser realizadas
de trás para frente, isto é, o último deverá ser o primeiro elemento removido.
*/

void Inserir_l1(int* lista, int* n, int max, int valor) {
    if (*n >= max) {
        printf("Lista cheia\n");
        return;
    }

    lista[*n] = valor;
    *n += 1;
}

void Remover_l1(int* lista, int* n) {
    if (*n <= 0) {
        printf("Lista vazia\n");
        return;
    }

    *n -= 1;
}