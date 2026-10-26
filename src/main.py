import numpy as np
from physics import electric_field
from visualization import plot_electric_field

def main():
    charges = [
        {"q": 1e-9, "x": -1.0, "y": 1.0},
        {"q": -1e-9, "x": 1.0, "y": 1.0},
        {"q": 1e-9, "x": 1.0, "y": -1.0},
        {"q": -1e-9, "x": -1.0, "y": -1.0},
        
    ]

    x = np.linspace(-3, 3, 300)
    y = np.linspace(-2, 2, 250)
    X, Y = np.meshgrid(x, y)

    Ex, Ey = electric_field(X, Y, charges)

    plot_electric_field(x, y, X, Y, Ex, Ey, charges)

if __name__ == "__main__":
    main()