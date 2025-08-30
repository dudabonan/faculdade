#include <stdio.h>

void Trocar(int *a, int *b) {
    int aux = *a;
    *a = *b;
    *b = aux;
}

void bubbleSort(int lista[], int tam) {
    int ord = 0;
    while (ord == 0) {
        ord = 1;
        for (int i = 0; i < tam-1; i++) {
            if (lista[i] > lista[i + 1]) {
                Trocar (&lista[i], &lista[i + 1]);
                ord = 0;
            }
        }
    }
}

void Imprimir(int l[], int tam) {
    for (int i = 0; i < tam; i++)
        printf("%d ", l[i]);

    printf("\n");
}

int main () {
    int vet[] = {32, 16, 48, 24, 8, 12, 4};
    int tamanho = sizeof(vet) / sizeof(vet[0]);
    
    printf("\nOriginal: ");
    Imprimir(vet, tamanho);
    
    bubbleSort(vet, tamanho);
    
    printf("Ordenado: ");
    Imprimir(vet, tamanho);
    printf("\n");
    
    return 0;
}