#include "funcionario.h"

// .\output\programa.exe

int main() {
    funcionario* lista = (funcionario*) malloc(sizeof(funcionario) * Tam);
    int nF = 0;
    int opcao = 0;
    int chave = 0;

    do {
        menu(&opcao);

        switch (opcao) {
            case 1:
                Cadastrar(lista, &nF, Tam);
                break;
            case 2:
                printf("Digite o ID do funcionario que voce deseja remover: ");
                scanf("%d", &chave);
                Remover(lista, &nF, chave);
                break;
            case 3:
                printf("Digite o ID do funcionario que voce deseja alterar o salario: ");
                scanf("%d", &chave);
                Alterar(lista, &nF, chave);
                break;
            case 4:
                printf("Digite o ID do funcionario que voce deseja imprimir: ");
                scanf("%d", &chave);
                Imprimir(lista, &nF, chave);
                break;
            case 5:
                break;

            default:
                printf("Opcao invalida!\n");
        }
    } while(opcao != 5);

    free(lista);
    return 0;
}