#include <stdio.h>

void Merge(int lista[], int ini, int meio, int fim) {
    int tam = fim-ini+1;
    int* auxL = (int*) malloc(tam * sizeof(int));
    int p1 = ini;
    int p2 = meio+1;

    for (int i = 0; i < tam; i++)
        if (p1 <= meio && p2 <= fim)
            if (lista[p1] < lista[p2])
                auxL[i] = lista[p1++];
            else 
                auxL[i] = lista[p2++];
        else
            if (p1 <= meio)
                auxL[i] = lista[p1++];
            else
                auxL[i] =lista[p2++];
    
    for (int i = 0; i < tam; i++)
        lista[ini + i] = auxL[i];

    free(auxL);
}

void mergeSort(int lista[], int ini, int fim) {
    if (ini < fim) {
        int meio = (ini + fim) / 2;
        mergeSort(lista, ini, meio);
        mergeSort(lista, meio+1, fim);
        Merge(lista, ini, meio, fim);
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
    
    mergeSort(vet, 0, tamanho-1);
    
    printf("Ordenado: ");
    Imprimir(vet, tamanho);
    printf("\n");
    
    return 0;
}