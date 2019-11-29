import numpy as np
import matplotlib.pyplot as plt


class ChaosGame:
    """A class for a chaos game.

    Parameters
    -----------
    n : int, default: 3
        Number of sides in n-gon.
    r : float, default: 1/2
        Ratio between two points on.
    """

    def __init__(self, n=3, r=1 / 2):
        self.n = n
        self.r = r

        if type(n) != int:
            raise ValueError("n must be an integer")
        if not 0 < r < 1:
            raise ValueError("r must be on (0,1) interval")
        if n < 1:
            raise ValueError(f"n must be larger than one. n:{n}")

        self._generate_ngon()

    def _generate_ngon(self):
        """Generates corners of n-gon."""
        n = self.n
        theta = np.linspace(0, 2 * np.pi, n + 1)
        c = np.zeros((n, 2))

        for i in range(n):
            c[i] = (np.sin(theta[i]), np.cos(theta[i]))

        self.c = c

    def plot_ngon(self):
        """Plots corners of n-gon."""
        plt.scatter(*zip(*self.c))
        plt.axis("equal")
        plt.show()

    def _starting_point(self):
        """Generates a starting point inside n-gon."""
        n = self.n
        w = np.random.random(n)
        w /= np.sum(w)

        return np.dot(w, self.c)

    def iterate(self, steps, discard=5):
        """Generates n points in n-gon.

        Parameters
        -----------
        steps : int
            Number of (x,y) points to be generated.
        discard : int, default: 5
            Number of first points from starting point to be discarded.

        Notes
        ------
        This method returns nothing, but stores but stores (x,y) points
        and corner corresponding points internally in the class.
        """
        r = self.r
        c = self.c
        k = np.random.randint(self.n, size=steps)

        x = np.zeros((steps, 2))
        x[0] = self._starting_point()

        for i in range(1, steps):
            x[i] = (r * x[i - 1]) + ((1 - r) * c[k[i]])
        self.x, self.k = x[discard:], k[discard:]

    @property
    def x_values(self):
        try:
            return self.x[:, 0]
        except AttributeError:
            raise AttributeError("Iterate method must be called to get x-values.")

    @property
    def y_values(self):
        try:
            return self.x[:, 1]
        except AttributeError:
            raise AttributeError("Iterate method must be called to get y-values.")

    @property
    def color(self):
        try:
            return self.col
        except AttributeError:
            return self._compute_color(self.k)

    def plot(self, color=False, cmap="jet"):
        """Plot for chaos game.

        Parameters
        ----------
        color : bool, default: False
            XXXXXXXXXXXXXXXXXXXXXXXXXX
        cmap : str, default: "jet"
            Matplotlib colormap.
        """
        try:
            x, k = self.x, self.k
        except AttributeError:
            raise AttributeError("Iterate method must be called.")

        fig, ax = plt.subplots()
        if color:
            g = self._compute_color(k)
            ax.scatter(*zip(*x), marker=".", s=0.2, cmap=cmap, c=g)
        else:
            ax.scatter(*zip(*x), marker=".", s=0.2, c="black")

        plt.axis("equal")
        plt.axis("off")
        self.fig = fig

    def _compute_color(self, k):
        """Generates list of gradient color values corresponding to x points"""
        col = np.empty(len(k))
        col[0] = k[0]
        for i in range(1, len(k)):
            col[i] = (col[i - 1] + k[i]) / 2

        return col

    def show(self, color=False, cmap="jet"):
        self.plot(color, cmap)
        plt.show()

    #NOT FINISHED
    def savepng(self, outfile, color=False, cmap="jet"):
        self.show(color, cmap)
        self.fig.savefig(outfile, dpi=300)


if __name__ == "__main__":

    test = ChaosGame(n=6, r=1/3)
    test.iterate(steps=100_000)
    test.show(color=True, cmap="twilight")
