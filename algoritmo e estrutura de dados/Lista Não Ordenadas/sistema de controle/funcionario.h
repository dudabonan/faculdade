#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define Tam 10

typedef struct {
    int dia;
    int mes;
    int ano;
} data;

typedef struct {
    int id;
    data aniversario;
    char nome[200];
    float salario;
    int carga_horaria;
} funcionario;

void menu(int* opcao);
int Cadastrar(funcionario* lista, int* nF, int tamanho);
int Remover(funcionario* lista, int* nF, int chave);
int Buscar(funcionario* lista, int* nF, int chave);
int Alterar(funcionario* lista, int* nF, int chave);
int Imprimir(funcionario* lista, int* nF, int chave);
