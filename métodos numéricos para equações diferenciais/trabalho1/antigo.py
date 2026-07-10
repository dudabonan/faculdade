import numpy as np 
from integrador_rk4 import derivadas, rk4
from plot_trajetorias import plot_poincare

def executar_poincare():
    mu = 0.012150
    w0 = np.array([0.994, 0.0, 0.0, -2.011752])
    t_final = 44 * np.pi
    h = 0.0001

    t, w = rk4(derivadas, 0.0, w0, t_final, h, mu) 

    poincare_x = []
    poincare_u = []

    for i in range(1, len(t)):
        y_ant = w[i-1, 1]
        y_atu = w[i, 1]
        v_atu = w[i, 3]

        if y_ant < 0 and y_atu >= 0 and v_atu > 0: 
            frac = -y_ant / (y_atu - y_ant)
            x_cruzamento = w[i-1, 0] + frac * (w[i, 0] - w[i-1, 0])
            u_cruzamento = w[i-1, 2] + frac * (w[i, 2] - w[i-1, 2])

            poincare_x.append(x_cruzamento)
            poincare_u.append(u_cruzamento)

    plot_poincare(poincare_x, poincare_u)
    

"""

import matplotlib.pyplot as plt 
import numpy as np
from integrador_rk4 import rk4, derivadas, jacobi_integral

def plotar_resultados(passos, h, mu, w0, periodo): 
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    for h_atual in passos: 
        t, w = rk4(derivadas, 0.0, w0, periodo * 3, h_atual, mu)

        idx_1periodo = int(periodo/h_atual)
        x, y = w[:idx_1periodo, 0], w[:idx_1periodo, 1]

        if h_atual == passos[0]: 
            ax1.plot(x, y, label="Trajetória - Órbita de Arenstorf", linewidth=1.2, color='lightcoral')
            ax1.plot(w0[0], w0[1], 's', markersize=7, label="Condição inicial", color='violet')
            ax1.plot(-mu, 0, 'o', label=r"$P_1$ - Terra (massa 1-µ)", color='teal')
            ax1.plot(1 - mu, 0, 'o', label=r"$P_2$ - Lua (massa µ)", color='indigo')

            print(f"\n--- Análise para h = {h_atual} ---")
            print(f"Estado Inicial:         {w0}")
            print(f"Estado após 1 Período:  {w[idx_1periodo]}")
            print(f"Estado após 2 Períodos: {w[int(2*periodo/h_atual)]}")
            print(f"Estado após 3 Períodos: {w[-1]}")
        
        cj = jacobi_integral(w, mu)
        erro_relativo = np.abs(cj - cj[0]) / np.abs(cj[0])
        ax2.plot(t, erro_relativo, label=f'h = {h_atual}')

    ax1.set_title(f"Problema Restrito dos Três Corpos  —  µ = {mu}\nRK4  |  $h={passos[0]}$  |  $t \\in [0, 5.432π]$  |  CI = ({w0[0]:.4f}, {w0[1]:.4f}, {w0[2]:.4f}, {w0[3]:.4f})", fontsize=10, pad=15)
    ax1.set_xlabel("x (adimensional)", fontsize=9)
    ax1.set_ylabel("y (adimensional)", fontsize=9)
    ax1.legend(fontsize=8)
    ax1.grid()

    ax2.set_title("Erro Relativo na Integral de Jacobi", fontsize=9, pad=15)
    ax2.set_xlabel("Tempo $t/\\pi$", fontsize=9)
    ax2.set_ylabel("Erro relativo $|\Delta C_J / C_{J,0}|$", fontsize=9)
    ax2.set_yscale('log')
    ax2.legend()
    ax2.grid()

    plt.tight_layout()
    plt.show()

def plot_poincare(poincare_x, poincare_u): 
    plt.figure(figsize=(7, 5))
    plt.plot(poincare_x, poincare_u, '.', markersize=5, color='lightcoral')
    plt.title("Seção de Poincaré (Órbita Original (y = 0, v > 0))  —  $t \\in [0, 44π]$", fontsize=10, pad=15)
    plt.xlabel("x", fontsize=9)
    plt.ylabel("u", fontsize=9)
    plt.grid()
    plt.show()
    
def plot_perturbacoes(perturbacao_x, perturbacao_u, e): 
    plt.figure(figsize=(5, 4))
    plt.plot(perturbacao_x, perturbacao_u, '.', markersize=4, label=f'ε = {e}', color='lightcoral')
    plt.title("Seção de Poincaré (Órbita Perturbada)  —  $t \\in [0, 44π]$", fontsize=10, pad=15)
    plt.xlabel("x", fontsize=9)
    plt.ylabel("u", fontsize=9)
    plt.grid()
    plt.legend()
    plt.tight_layout()
    plt.show()

def plot_lagrange(x, y, mu):
    cor_fundo = '#11151c'
    plt.figure(figsize=(7, 5))
    plt.plot(x, y, label=f'Trajetória (μ = {mu})', color='violet')
    
    L4_x = 0.5 - mu
    L4_y = np.sqrt(3) / 2
    plt.plot(L4_x, L4_y, 'o', markersize=5, label=r'$L_4$', color='indigo')
    
    plt.title(rf"Estabilidade em torno de $L_4$  —  $t \in [0, 70π]$", fontsize=10, pad=15)
    plt.xlabel("x", fontsize=9)
    plt.ylabel("y", fontsize=9)
    plt.legend(fontsize=9)
    plt.grid()
    plt.tight_layout()
    plt.axis('equal')
    plt.show()

"""