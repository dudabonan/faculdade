import numpy as np

from integrador_rk4 import rk4, derivadas
from plot_trajetorias import plot_perturbacoes_comparativo, plot_lagrange_comparativo
from secao_poincare import secao_poincare

def executar_perturbacoes():
    # definindo as condições iniciais
    mu = 0.012150
    w0 = np.array([0.994, 0.0, 0.0, -2.011752])
    h = 0.0001
    tf = 44 * np.pi
    
    e = [1e-6, 1e-5, 1e-4, 1e-3] # diferentes ordens de grandeza para perturbação
    
    resultados = []
    for epsilon in e:
        # aplicando a perturbação na condição inicial
        w0_perturbado = w0 + np.array([epsilon, 0.0, 0.0, 0.0])
        
        # integrando o sistema com a condição inicial perturbada
        t, w = rk4(derivadas, 0.0, w0_perturbado, tf, h, mu)
        
        pp_x, pp_u = secao_poincare(t, w) # obtendo a seção de Poincaré
        
        resultados.append((epsilon, w[:, 0], w[:, 1], pp_x, pp_u))
        
    plot_perturbacoes_comparativo(resultados, mu, w0)

def executar_lagrange():
    # definindo os parâmetros
    delta = 0.01
    massa = [0.01, 0.0385, 0.04]
    
    h = 0.001
    Ti, Tf = 0, 70 * np.pi
    
    resultados = {}
    
    for mu in massa:
        resultados[mu] = []
        
        # calculando as coordenadas iniciais de L4
        x0 = 0.5 - mu + delta
        y0 = np.sqrt(3) / 2
        w0 = np.array([x0, y0, 0.0, 0.0]) # vetor de estado inicial

        _, w = rk4(derivadas, Ti, w0, Tf, h, mu) # integrando o sistema
        x, y = w[:, 0], w[:, 1]

        resultados[mu].append((x, y))

    plot_lagrange_comparativo(resultados, massa)