#include <stdio.h>

void Trocar(int *a, int *b) {
    int aux = *a;
    *a = *b;
    *b = aux;
}

void quickSort(int lista[], int ini, int fim) {
    if (ini < fim) {
        // escolhe o pivô e coloca no final
        int pivo = lista[(ini + fim) / 2];
        Trocar(&lista[(ini + fim) / 2], &lista[fim]);

        int i = ini;
        int f = fim - 1;

        while (f >= i) {
            while (lista[i] < pivo)
                i++;
            while (lista[f] > pivo)
                f--;

            if (f >= i) {
                Trocar(&lista[i], &lista[f]);
                i++;
                f--;
            }
        }
        // coloca o pivô na posição certa
        Trocar(&lista[fim], &lista[i]);

        // chama recursivamente para as sub-listas
        quickSort(lista, ini, i-1);
        quickSort(lista, i+1, fim);
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
    
    quickSort(vet, 0, tamanho-1);
    
    printf("Ordenado: ");
    Imprimir(vet, tamanho);
    printf("\n");
    
    return 0;
}