import os 
import time 
import numpy as np
import matplotlib.pyplot as plt

from plot_trajetorias import plotar_resultados
from secao_poincare import executar_poincare
from estatisticas import executar_perturbacoes, executar_lagrange

def executar_arenstorf():
    mu = 0.012150
    w0 = np.array([0.994, 0.0, 0.0, -2.011752])
    passos = [0.0001, 0.001]
    periodo = 5.432 * np.pi 
    
    plotar_resultados(passos, 0.0001, mu, w0, periodo)

def limpar_tela(): 
    os.system('cls' if os.name == 'nt' else 'clear')

def cabecalho(): 
    limpar_tela()
    print("======="*10)
    print(" "*14 + "Simulador:  Problema Restrito de 3 Corpos ")
    print("======="*10)

def pausar():
    input("\nPressione [ENTER] para voltar ao menu principal...")

def main():
    while True:
        cabecalho()
        print("Escolha qual simulação deseja executar:")
        print("  1. Órbita de Arenstorf e Integral de Jacobi")
        print("  2. Construção da Seção de Poincaré")
        print("  3. Estabilidade 1 (Sensibilidade a Perturbações)")
        print("  4. Estabilidade 2 (Pontos de Lagrange L4)")
        print("  0. Sair\n")
        
        opcao = input("Digite o número da opção desejada: ")

        if opcao == '1':
            print("\nIniciando Atividade 1...")
            executar_arenstorf() 
            pausar()
        elif opcao == '2':
            print("\nIniciando Atividade 2...")
            executar_poincare()
            pausar()
        elif opcao == '3':
            print("\nIniciando Atividade 3...")
            executar_perturbacoes()
            pausar()
        elif opcao == '4':
            print("\nIniciando Atividade 4...")
            executar_lagrange()
            pausar()
        elif opcao == '0':
            print("\nEncerrando o simulador. Até logo!\n")
            break
        else:
            print("\nOpção inválida! Tente novamente.")
            time.sleep(1.5)

if __name__ == "__main__":
    plt.ion() 
    main()