import matplotlib.pyplot as plt 
import numpy as np
from integrador_rk4 import rk4, derivadas, jacobi_integral

def plotar_resultados(passos, h, mu, w0, periodo):
    plt.style.use('dark_background')
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    for h_atual in passos:
        # integrando o sistema com o passo atual
        t, w = rk4(derivadas, 0.0, w0, periodo * 3, h_atual, mu)

        # índices correspondentes a 1, 2 e 3 períodos
        idx_1periodo = int(round(periodo / h_atual))
        idx_2periodos = int(round(2 * periodo / h_atual))
        idx_3periodos = min(int(round(3 * periodo / h_atual)), len(w) - 1)
        
        # integral de Jacobi e erro relativo
        cj = jacobi_integral(w, mu)
        erro_relativo = np.abs(cj - cj[0]) / np.abs(cj[0])

        # definindo a largura das colunas para ajeitar a tabela
        c1, c2, c3, c4 = 12, 50, 20, 20
        lt = c1 + c2 + c3 + c4 + 6

        print(f"\n{'Análise para h = ' + str(h_atual):^{lt}}\n")
        print(f"{'Instante':^{c1}} | {'Estado':^{c2}} | {'Desvio |w - w0|':^{c3}}| {'Erro Relativo':^{c4}}")
        print("-" * lt)
        print(f"{'Inicial':^{c1}} | {str(w0):^{c2}} | {np.linalg.norm(w0 - w0):^{c3}.6e}| {erro_relativo[0]:^{c4}.6e}")
        print(f"{'1 Período':^{c1}} | {str(w[idx_1periodo]):^{c2}} | {np.linalg.norm(w[idx_1periodo] - w0):^{c3}.6e}| {erro_relativo[idx_1periodo]:^{c4}.6e}")
        print(f"{'2 Períodos':^{c1}} | {str(w[idx_2periodos]):^{c2}} | {np.linalg.norm(w[idx_2periodos] - w0):^{c3}.6e}| {erro_relativo[idx_2periodos]:^{c4}.6e}")
        print(f"{'3 Períodos':^{c1}} | {str(w[idx_3periodos]):^{c2}} | {np.linalg.norm(w[idx_3periodos] - w0):^{c3}.6e}| {erro_relativo[idx_3periodos]:^{c4}.6e}\n")

        if h_atual == passos[0]:
            x, y = w[:idx_3periodos, 0], w[:idx_3periodos, 1]
            ax1.plot(x, y, label="Trajetória", linewidth=0.7, color='lightcoral', alpha=0.85)
            ax1.plot(w0[0], w0[1], '+', markersize=12, label="Condição inicial", color='gold')
            ax1.plot(-mu, 0, 'o', label=r"$P_1$ - Terra (massa 1-µ)", color='plum')
            ax1.plot(1 - mu, 0, 'o', label=r"$P_2$ - Lua (massa µ)", color='aquamarine')

            pontos_periodo = [
                (idx_1periodo, "Após 1 período",  'white'),
                (idx_2periodos, "Após 2 períodos", 'deepskyblue'),
                (idx_3periodos, "Após 3 períodos", 'limegreen'),
            ]
            for idx_p, rotulo, cor in pontos_periodo:
                ax1.plot(w[idx_p, 0], w[idx_p, 1], 'x', markersize=9, markeredgewidth=2, color=cor, label=rotulo, zorder=5)
                ax1.annotate(rotulo, (w[idx_p, 0], w[idx_p, 1]), textcoords="offset points", xytext=(6, 6), fontsize=7, color=cor)

        # plot da curva do erro de Jacobi
        ax2.plot(t, erro_relativo, label=f'h = {h_atual}', linewidth=1, color='coral' if h_atual == passos[0] else 'lightblue')

    # simulação da trajetória
    ax1.set_title(f"Problema Restrito dos Três Corpos  —  µ = {mu}\nRK4  |  $h={passos[0]}$  |  $t \\in [0, 3\\times5.432π]$  |  CI = ({w0[0]:.4f}, {w0[1]:.4f}, {w0[2]:.4f}, {w0[3]:.4f})", fontsize=10, pad=15)
    ax1.set_xlabel("x (adimensional)", fontsize=9)
    ax1.set_ylabel("y (adimensional)", fontsize=9)
    ax1.legend(fontsize=8)
    ax1.grid(alpha=0.3)
    ax1.axis('equal')

    ax2.set_title("Erro Relativo na Integral de Jacobi", fontsize=10, pad=15)
    ax2.set_xlabel("Tempo $t/\\pi$", fontsize=9)
    ax2.set_ylabel(r"Erro relativo $|\Delta C_J / C_{J,0}|$", fontsize=9)
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
    
def plot_perturbacoes_comparativo(resultados, mu, w0_original):
    plt.style.use('dark_background')
    n = len(resultados)
    fig, axes = plt.subplots(2, n, figsize=(4 * n, 8))

    for i, (epsilon, x, y, px, pu) in enumerate(resultados):
        ax_traj = axes[0, i]
        ax_poin = axes[1, i]

        # plano físico x-y
        ax_traj.plot(x, y, linewidth=0.5, color='lightcoral')
        ax_traj.plot(w0_original[0], w0_original[1], '+', markersize=9, color='gold')
        ax_traj.plot(-mu, 0, 'o', markersize=5, color='plum')
        ax_traj.plot(1 - mu, 0, 'o', markersize=5, color='aquamarine')
        ax_traj.set_title(f"ε = {epsilon}", fontsize=9)
        ax_traj.set_xlabel("x", fontsize=8)
        ax_traj.set_ylabel("y" if i == 0 else "", fontsize=8)
        ax_traj.grid(alpha=0.3)
        ax_traj.axis('equal')

        # Seção de Poincaré
        ax_poin.plot(px, pu, '.', markersize=4, color='lightcoral')
        ax_poin.set_xlabel("x", fontsize=8)
        ax_poin.set_ylabel("u" if i == 0 else "", fontsize=8)
        ax_poin.grid(alpha=0.3)

    fig.suptitle("Sensibilidade a Perturbações\n" "Linha de cima: plano x-y  |  Linha de baixo: Seção de Poincaré (y=0, v>0)  —  $t \\in [0, 44π]$", fontsize=10)
    plt.tight_layout()
    plt.show()

def plot_lagrange_comparativo(resultados, mu_lista):
    plt.style.use('dark_background')
    n = len(mu_lista)
    fig, axes = plt.subplots(1, n, figsize=(5.5 * n, 5))
    if n == 1:
        axes = [axes]

    for ax, mu in zip(axes, mu_lista):
        for x, y in resultados[mu]:
            ax.plot(x, y, label=f'Trajetória (δ = 0.01)', color='lightcoral', linewidth=0.7)

            # coordenadas do ponto L4
            L4_x = 0.5 - mu
            L4_y = np.sqrt(3) / 2
            ax.plot(L4_x, L4_y, 'o', markersize=6, label=r'$L_4$', color='aquamarine')

            ax.set_title(rf"µ = {mu}", fontsize=10)
            ax.set_xlabel("x", fontsize=9)
            ax.set_ylabel("y", fontsize=9)
            ax.legend(loc='upper right', fontsize=8)
            ax.grid(alpha=0.3)
            ax.axis('equal')

    fig.suptitle("Estabilidade em torno de $L_4$ para diferentes massas (µ)", fontsize=11)
    plt.tight_layout()
    plt.show()