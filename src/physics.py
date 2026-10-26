import numpy as np

K_COULOMB = 8.9875517923e9

def electric_field(X, Y, charges):
    Ex = np.zeros_like(X, dtype=float)
    Ey = np.zeros_like(Y, dtype=float)

    for charge in charges:
        q = charge["q"]
        x0 = charge["x"]
        y0 = charge["y"]

        dx = X - x0
        dy = Y - y0

        r_squared = dx**2 + dy**2
        
        r_squared = np.maximum(r_squared, 1e-12)

        r_cubed = r_squared**1.5

        Ex += K_COULOMB * q * dx / r_cubed
        Ey += K_COULOMB * q * dy / r_cubed

    return Ex, Ey