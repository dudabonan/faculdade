import numpy as np 
from integrador_rk4 import derivadas, rk4
from plot_trajetorias import plot_poincare

def secao_poincare(t, w):
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
            
    return poincare_x, poincare_u

def executar_poincare():
    mu = 0.012150
    w0 = np.array([0.994, 0.0, 0.0, -2.011752])
    t_final = 44 * np.pi
    h = 0.0001

    t, w = rk4(derivadas, 0.0, w0, t_final, h, mu)
    poincare_x, poincare_u = secao_poincare(t, w)
    
    plot_poincare(poincare_x, poincare_u)