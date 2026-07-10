import numpy as np 

def derivadas(t, estado, mu):
    x, y, u, v = estado

    r1 = np.sqrt((x+mu)**2 + y**2)
    r2 = np.sqrt((x-1 + mu)**2 + y**2)

    dxdt = u 
    dydt = v
    dudt = 2*v + x - ((1 - mu) * (x + mu)) / r1**3 - (mu * (x - 1 + mu)) / r2**3 
    dvdt = -2*u + y - ((1 - mu) * y) / r1**3 - (mu * y) / r2**3

    return np.array([dxdt, dydt, dudt, dvdt])

def rk4(f, t0, y0, tf, h, mu): 
    t_vals = np.arange(t0, tf, h)
    y_vals = np.zeros((len(t_vals), len(y0)))
    y_vals[0] = y0

    for i in range(1, len(t_vals)): 
        t_atual = t_vals[i-1]
        y_atual = y_vals[i-1]

        k1 = h * f(t_atual, y_atual, mu)
        k2 = h * f(t_atual + h/2, y_atual + k1/2, mu)
        k3 = h * f(t_atual + h/2, y_atual + k2/2, mu)
        k4 = h * f(t_atual + h, y_atual + k3, mu)

        y_vals[i] = y_atual + (k1 + 2*k2 + 2*k3 + k4) / 6.0
    
    return t_vals, y_vals 

def jacobi_integral(w, mu): 
    x, y, u, v = w.T

    r1 = np.sqrt((x + mu)**2 + y**2)
    r2 = np.sqrt((x-1 + mu)**2 + y**2)

    return (x**2 + y**2) + 2*(1-mu)/r1 + 2*mu/r2 - (u**2 + v**2)