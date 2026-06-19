import numpy as np

def heat_equation(u, sigma, dx):
    dudt = np.zeros_like(u)

    # boundary conditions
    dudt[0] = 0
    dudt[-1] = 0

    for i in range(1, len(u)-1):
        dudt[i] = sigma * (
            u[i-1] - 2*u[i] + u[i+1]
        ) / dx**2

    return dudt