import matplotlib.pyplot as plt 
import numpy as np
from integrador_rk4 import rk4, derivadas, jacobi_integral

def plotar_resultados(passos, h, mu, w0, periodo):
    plt.style.use('dark_background')
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    for h_atual in passos:
        t, w = rk4(derivadas, 0.0, w0, periodo * 3, h_atual, mu)

        idx_1periodo = int(periodo/h_atual)
        x, y = w[:idx_1periodo, 0], w[:idx_1periodo, 1]

        if h_atual == passos[0]:
            ax1.plot(x, y, label="Trajetória - Órbita de Arenstorf", linewidth=1, color='lightcoral')
            ax1.plot(w0[0], w0[1], '+', markersize=12, label="Condição inicial", color='gold')
            ax1.plot(-mu, 0, 'o', label=r"$P_1$ - Terra (massa 1-µ)", color='plum')
            ax1.plot(1 - mu, 0, 'o', label=r"$P_2$ - Lua (massa µ)", color='aquamarine')

            print(f"\n--- Análise para h = {h_atual} ---")
            print(f"Estado Inicial:         {w0}")
            print(f"Estado após 1 Período:  {w[idx_1periodo]}")
            print(f"Estado após 2 Períodos: {w[int(2*periodo/h_atual)]}")
            print(f"Estado após 3 Períodos: {w[-1]}")
        
        cj = jacobi_integral(w, mu)
        erro_relativo = np.abs(cj - cj[0]) / np.abs(cj[0])
        ax2.plot(t, erro_relativo, label=f'h = {h_atual}', linewidth=1, color='coral' if h_atual == passos[0] else 'lightblue')

    ax1.set_title(f"Problema Restrito dos Três Corpos  —  µ = {mu}\nRK4  |  $h={passos[0]}$  |  $t \\in [0, 5.432π]$  |  CI = ({w0[0]:.4f}, {w0[1]:.4f}, {w0[2]:.4f}, {w0[3]:.4f})", fontsize=10, pad=15)
    ax1.set_xlabel("x (adimensional)", fontsize=9)
    ax1.set_ylabel("y (adimensional)", fontsize=9)
    ax1.legend(fontsize=8)
    ax1.grid(alpha=0.3)

    ax2.set_title("Erro Relativo na Integral de Jacobi", fontsize=10, pad=15)
    ax2.set_xlabel("Tempo $t/\\pi$", fontsize=9)
    ax2.set_ylabel("Erro relativo $|\Delta C_J / C_{J,0}|$", fontsize=9)
    ax2.set_yscale('log')
    ax2.legend(fontsize=8)
    ax2.grid(alpha=0.3)

    plt.tight_layout()
    plt.show()

def plot_poincare(poincare_x, poincare_u):
    plt.style.use('dark_background')
    plt.figure(figsize=(7, 5))
    plt.plot(poincare_x, poincare_u, '.', markersize=5, color='lightcoral')
    plt.title("Seção de Poincaré (Órbita Original (y = 0, v > 0))  —  $t \\in [0, 44π]$", fontsize=10, pad=15)
    plt.xlabel("x", fontsize=9)
    plt.ylabel("u", fontsize=9)
    plt.grid(alpha=0.3)
    plt.show()
    
def plot_perturbacoes(perturbacao_x, perturbacao_u, e):
    plt.style.use('dark_background')
    plt.figure(figsize=(7, 5))
    plt.plot(perturbacao_x, perturbacao_u, '.', markersize=5, label=f'ε = {e}', color='lightcoral')
    plt.title("Seção de Poincaré (Órbita Perturbada)  —  $t \\in [0, 44π]$", fontsize=10, pad=15)
    plt.xlabel("x", fontsize=9)
    plt.ylabel("u", fontsize=9)
    plt.grid(alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.show()

def plot_lagrange(x, y, mu):
    plt.style.use('dark_background')
    plt.figure(figsize=(7, 5))
    plt.plot(x, y, label='Trajetória', color='lightcoral', linewidth=0.5)
    
    L4_x = 0.5 - mu
    L4_y = np.sqrt(3) / 2
    plt.plot(L4_x, L4_y, 'o', markersize=5, label=r'$L_4$', color='aquamarine')
    
    plt.title(rf"Estabilidade em torno de $L_4$  —  μ = {mu}", fontsize=10, pad=15)
    plt.xlabel("x", fontsize=9)
    plt.ylabel("y", fontsize=9)
    plt.legend(fontsize=9)
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.axis('equal')
    plt.show()