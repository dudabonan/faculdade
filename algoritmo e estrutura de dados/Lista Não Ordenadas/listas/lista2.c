#include "lista2.h"
#include <stdio.h>

/*
Os elementos devem ser inseridos no final da lista. As remoções devem ser realizadas
de frente para trás sem deixar espaços vazios. Isto é, o primeiro elemento da lista deverá
ser removido e todos os seguintes devem ser deslocados uma posição a frente.
*/

void Inserir_l2(int* lista, int* n, int max, int valor) {
    if (*n >= max) {
        printf("Lista cheia\n");
        return;
    }

    lista[*n] = valor;
    *n += 1;
}

void Remover_l2(int* lista, int* n) {
    if (*n <= 0) {
        printf("Lista vazia\n");
        return;
    }
    
    for (int i = 0; i < *n-1; i++)
        lista[i] = lista[i+1];

    *n -= 1;
}