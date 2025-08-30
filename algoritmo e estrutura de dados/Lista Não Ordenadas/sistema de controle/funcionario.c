#include <stdio.h>
#include "funcionario.h"

void menu(int* opcao) {
    printf("\n\n-=-=-=- MENU -=-=-=-\n");
    printf("1 - Cadastrar Funcionario\n");
    printf("2 - Remover Funcionario\n");
    printf("3 - Alterar Salario\n");
    printf("4 - Imprimir Dados do Funcionario\n");
    printf("5 - Sair\n");
    printf("-=-=-=-=-=-=-=-=-=-=-\n");

    printf("\nEscolha uma opcao: ");
    scanf("%d", opcao);
}

int Cadastrar(funcionario* lista, int* nF, int tamanho) {
    if (*nF < tamanho) {
        printf("\nDados do funcionario: \n");
        printf("ID: ");
        scanf("%d", &lista[*nF].id);

        printf("Nome: ");
        fflush(stdin);
        fgets(lista[*nF].nome, 200, stdin);

        printf("Data de nascimento (dd/mm/yyyy): \n");
        scanf("%d", &lista[*nF].aniversario.dia);
        scanf("%d", &lista[*nF].aniversario.mes);
        scanf("%d", &lista[*nF].aniversario.ano);

        printf("Salario: ");
        scanf("%f", &lista[*nF].salario);

        printf("Carga Horaria: ");
        scanf("%d", &lista[*nF].carga_horaria);

        printf("Funcionario cadastrado com sucesso!");
        *nF += 1;

        return 0;
    }
    else {
        printf("Lista cheia!");
        return -1;
    }
}

int Buscar(funcionario* lista, int* nF, int chave) {
    int i = 0;
    while(i < *nF) {
        if(lista[i].id == chave) {
            return i;
        }
        i++;
    }

    return -1;
}

int Remover(funcionario* lista, int* nF, int chave) {
    int posicao = Buscar(lista, nF, chave);

    if(posicao == -1) {    
        printf("Esse ID nao esta cadastrado!");
        return -1;
    }

    lista[posicao] = lista[*nF - 1];
    *nF -= 1;
    printf("Remocao concluida!");
    return 1;
}

int Alterar(funcionario* lista, int* nF, int chave) {
    int posicao = Buscar(lista, nF, chave);

    if(posicao == -1)
        return -1;

    printf("Digite o novo valor: ");
    scanf("%f", &lista[posicao].salario);
    printf("Alteração realizada!");

    return 1;
}

int Imprimir(funcionario* lista, int* nF, int chave) {
    int posicao = Buscar(lista, nF, chave);

    if(posicao == -1) {    
        printf("Esse ID nao esta cadastrado!");
        return -1;
    }

    printf("\n-=-=- Funcionario: %d -=-=-", lista[posicao].id);
    printf("\n\nData:\t %d\\%d\\%d", lista[posicao].aniversario.dia, lista[posicao].aniversario.mes, lista[posicao].aniversario.ano);
    printf("\nNome:\t %s", lista[posicao].nome);
    printf("Salario: %.2f", lista[posicao].salario);
    printf("\ncH:\t %d", lista[posicao].carga_horaria);
    printf("\n\n-=-=-=-=-=-=-=-=-=-=-=-=-=-");
    return 1;
}
