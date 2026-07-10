import numpy as np

from integrador_rk4 import rk4, derivadas
from plot_trajetorias import plot_perturbacoes, plot_lagrange
from secao_poincare import secao_poincare

def executar_perturbacoes():
    mu = 0.012150
    w0 = np.array([0.994, 0.0, 0.0, -2.011752])
    h = 0.001
    tf = 44 * np.pi
    
    e = [1e-6, 1e-5, 1e-4, 1e-3]
    
    for epsilon in e:
        w0_perturbado = w0 + np.array([epsilon, 0.0, 0.0, 0.0])
        
        t, w = rk4(derivadas, 0.0, w0_perturbado, tf, h, mu)
        pp_x, pp_u = secao_poincare(t, w)
        
        plot_perturbacoes(pp_x, pp_u, epsilon)

def executar_lagrange():
    delta = 0.01
    massa = [0.01, 0.0385, 0.04]
    
    h = 0.001
    Ti, Tf = 0, 70 * np.pi
    
    for mu in massa:
        x0 = 0.5 - mu + delta
        y0 = np.sqrt(3) / 2
        
        w0 = np.array([x0, y0, 0.0, 0.0])
        
        _, w = rk4(derivadas, Ti, w0, Tf, h, mu)
        x, y = w[:, 0], w[:, 1]
        
        plot_lagrange(x, y, mu)