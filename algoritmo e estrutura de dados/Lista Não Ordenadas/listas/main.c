#include "lista1.h"
#include "lista2.h"
#include "lista3.h"
#include "lista4.h"

#define TAM 1000000

int main() {
    int *lista1 = (int*) malloc(sizeof(int) * TAM);
    int *lista2 = (int*) malloc(sizeof(int) * TAM);
    int *lista3 = (int*) malloc(sizeof(int) * TAM);
    int *lista4 = (int*) malloc(sizeof(int) * TAM);

    int n1 = 0, n2 = 0, n3 = 0, n4 = 0;
    srand(time(NULL));
    clock_t inicio, fim;
    double tempo;


    // LISTA 1
    inicio = clock();
    for (int i = 0; i < TAM; i++) {
        Inserir_l1(lista1, &n1, TAM, rand());
    }
    fim = clock();
    tempo = (double)(fim - inicio) / CLOCKS_PER_SEC;
    printf("\nTempo para preencher lista 1: %.2f segundos\n", tempo);

    inicio = clock();
    while (n1 > 0) {
        Remover_l1(lista1, &n1);
    }
    fim = clock();
    tempo = (double)(fim - inicio) / CLOCKS_PER_SEC;
    printf("Tempo para esvaziar lista 1: %.2f segundos\n\n", tempo);


    // LISTA 2
    inicio = clock();
    for (int i = 0; i < TAM; i++) {
        Inserir_l2(lista2, &n2, TAM, rand());
    }
    fim = clock();
    tempo = (double)(fim - inicio) / CLOCKS_PER_SEC;
    printf("Tempo para preencher lista 2: %.2f segundos\n", tempo);

    inicio = clock();
    while (n2 > 0) {
        Remover_l2(lista2, &n2);
    }
    fim = clock();
    tempo = (double)(fim - inicio) / CLOCKS_PER_SEC;
    printf("Tempo para esvaziar lista 2: %.2f segundos\n\n", tempo);


    // LISTA 3
    inicio = clock();
    for (int i = 0; i < TAM; i++) {
        Inserir_l3(lista3, &n3, TAM, rand());
    }
    fim = clock();
    tempo = (double)(fim - inicio) / CLOCKS_PER_SEC;
    printf("Tempo para preencher lista 3: %.2f segundos\n", tempo);

    inicio = clock();
    while (n1 > 0) {
        Remover_l3(lista3, &n3);
    }
    fim = clock();
    tempo = (double)(fim - inicio) / CLOCKS_PER_SEC;
    printf("Tempo para esvaziar lista 3: %.2f segundos\n\n", tempo);


    // LISTA 4
    inicio = clock();
    for (int i = 0; i < TAM; i++) {
        Inserir_l4(lista4, &n4, TAM, rand());
    }
    fim = clock();
    tempo = (double)(fim - inicio) / CLOCKS_PER_SEC;
    printf("Tempo para preencher lista 4: %.2f segundos\n", tempo);

    inicio = clock();
    while (n1 > 0) {
        Remover_l4(lista4, &n4);
    }
    fim = clock();
    tempo = (double)(fim - inicio) / CLOCKS_PER_SEC;
    printf("Tempo para esvaziar lista 4: %.2f segundos\n\n", tempo);

    free(lista1);
    free(lista2);
    free(lista3);
    free(lista4);

    return 0;
}

// gcc main.c lista1.c lista2.c lista3.c lista4.c -o output/complistas.exe
// .\output\complistas.exe