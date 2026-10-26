import numpy as np
import matplotlib.pyplot as plt

def plot_electric_field(x, y, X, Y, Ex, Ey, charges):

    E = np.sqrt(Ex**2 + Ey**2)

    fig, ax = plt.subplots(figsize=(11, 8))

    ax.streamplot(
        x,
        y,
        Ex,
        Ey,
        color=np.log10(np.maximum(E, 1e-10)),
        cmap="plasma",
        density=1.5,
        linewidth=1.0,
        arrowsize=1.2
    )

    for charge in charges:
        q = charge["q"]
        x0 = charge["x"]
        y0 = charge["y"]

        if q > 0:
            color = "red"
            label = f"+{q * 1e9:.1f} nC"
        else:
            color = "blue"
            label = f"{q * 1e9:.1f} nC"

        ax.scatter(
            x0,
            y0,
            s=180,
            color=color,
            edgecolors="black",
            zorder=5
        )

        ax.annotate(
            label,
            (x0, y0),
            xytext=(0, 12),
            textcoords="offset points",
            ha="center",
            fontsize=11,
            fontweight="bold"
        )

    ax.set_title("Electric Field of Multiple Point Charges", fontsize=15)
    ax.set_xlabel("x (m)")
    ax.set_ylabel("y (m)")

    ax.set_xlim(x[0], x[-1])
    ax.set_ylim(y[0], y[-1])

    ax.set_aspect("equal")
    ax.grid(True, alpha=0.2)

    colorbar = fig.colorbar(
        plt.cm.ScalarMappable(
            norm=plt.Normalize(
                vmin=np.log10(max(E.min(), 1e-10)),
                vmax=np.log10(max(E.max(), 1e-9))
            ),
            cmap="plasma"
        ),
        ax=ax
    )
    colorbar.set_label("log10(|E|)")

    plt.tight_layout()
    plt.show()