import numpy as np
import matplotlib.pyplot as plt
import chaos_game as chaos
import fern as fern


class Variations:
    """
    A class for remapping the plane.

    Parameters
    -----------
    x : n iterable
        x-coordinates
    y : n iterable
        y-coordinates corresponding to x
    colors : n color values, default: "black"
        Color for plotting x and y coordinates.
    """

    def __init__(self, x, y, colors="black"):
        try:
            iter(x)
        except:
            raise TypeError("(Variations) x is not an iterable")
        try:
            iter(y)
        except:
            raise TypeError("(Variations) y is not an iterable")
       # selfs
        # change dtype
        if type(x) != np.ndarray:
            self.x = np.array(x, dtype="float_")
        else:
            self.x = x
        if type(y) != np.ndarray:
            self.y = np.array(y, dtype="float_")
        else:
            self.y = y

        #scale
        scale = max((max(abs(y)), max(abs(x))))
        self.y = self.y / scale
        self.x = self.x / scale
      # public
        self.colors = colors
        self.collection = {
            "linear": self.linear,
            "handkerchief": self.handkerchief,
            "swirl": self.swirl,
            "disc": self.disc,
            "spherical": self.spherical,
            "sinusoidal": self.sinusoidal,
        }

    def __call__(self, coeffs):
        """Generates a linear combination of two variations with coefficients."""
        keys = list(coeffs)

        self.collection[keys[1]]()
        u1 = self.u.copy()
        v1 = self.v.copy()
        self.collection[keys[0]]()
        u2 = self.u.copy()
        v2 = self.v.copy()
        self._u = u1*coeffs[keys[1]] + u2*coeffs[keys[0]]
        self._v = v1*coeffs[keys[1]] + v2*coeffs[keys[0]]


   # Properties
    @property
    def u(self):
        """Returns u scaled with largest absolute value of given coordinates"""
        return self._u / self.scale

    @property
    def v(self):
        """Returns v scaled with largest absolute value of given coordinates"""
        return self._v / self.scale

    @property
    def scale(self):
        return max((max(abs(self._u)), max(abs(self._v))))

    @property
    def r(self):
        return np.sqrt(self.x ** 2 + self.y ** 2)

    @property
    def theta(self):
        return np.arctan2(self.x, self.y)

    @property
    def phi(self):
        return np.arctan2(self.y, self.x)

   # Variations
    def linear(self):
        self._u = self.x
        self._v = self.y

    def handkerchief(self):
        r, theta = self.r, self.theta
        self._u = r * np.sin(theta + r)
        self._v = r * np.cos(theta - r)

    def swirl(self):
        x, y = self.x, self.y
        r = self.r
        self._u = x * np.sin(r ** 2) - y * np.cos(r ** 2)
        self._v = x * np.cos(r ** 2) + y * np.sin(r ** 2)

    def disc(self):
        theta, r = self.theta, self.r
        self._u = (theta / np.pi) * np.sin(np.pi * r)
        self._v = (theta / np.pi) * np.cos(np.pi * r)

    # choose atleast two more to implement.
    def spherical(self):
        x, y = self.x, self.y
        r = self.r
        self._u = (1 / r ** 2) * x
        self._v = (1 / r ** 2) * y

    def sinusoidal(self):
        x, y = self.x, self.y
        self._u = np.sin(x)
        self._v = np.sin(y)

    def plot(self, cmap=None):
        """Generates plot using lates computed variation of coordinates."""
        plt.scatter(self.u, -self.v, c=self.colors, cmap=cmap, s=0.1)
        plt.axis("equal")
        plt.axis("off")


def plot_grid():
    """Generates plot of a uniformly spaced grid (-1,1)."""
    plt.plot([-1, 1, 1, -1, -1], [-1, -1, 1, 1, -1], color="grey")
    plt.plot([-1, 1], [0, 0], color="grey")
    plt.plot([0, 0], [-1, 1], color="grey")


def example_solution():
    """Example given in assignment, scaled."""
    N = 60
    grid_values = np.linspace(-1, 1, N)
    x_values = np.ones(N * N)
    y_values = np.ones(N * N)
    for i in range(N):
        index = i * N
        x_values[index : index + N] *= grid_values[i]
        y_values[index : index + N] *= grid_values

    coords_varia = Variations(x_values, y_values)

    variations = ["linear", "handkerchief", "swirl", "disc"]

    plt.figure(10, figsize=(9, 9))
    for i in range(4):
        plt.subplot(221 + i)
        plot_grid()
        variation = variations[i]
        coords_varia.collection[variation]()
        coords_varia.plot()
        plt.title(variation)
    plt.show()


def example_chaos():
    """Plot of different variations of n-gon, n=4."""
    test = chaos.ChaosGame(n=4, r=1/3)
    test.iterate(10000)
    x, y, color = test.x_values, test.y_values, test.color

    coords_varia = Variations(x, y, color)
    variations = ["linear", "handkerchief", "swirl", "disc"]

    plt.figure(10, figsize=(9, 9))
    for i in range(4):
        plt.subplot(221 + i)
        variation = (variations[i])
        coords_varia.collection[variation]()
        coords_varia.plot()
        plt.title(variation)
    plt.show()


def example_fern():
    """Plot of different variations of the Barnsley fern."""
    parameters = (
        (0, 0, 0, 0.16, 0, 0),
        (0.85, 0.04, -0.04, 0.85, 0, 1.60),
        (0.20, -0.26, 0.23, 0.22, 0, 1.60),
        (-0.15, 0.28, 0.26, 0.24, 0, 0.44),
    )
    distribution = (0.01, 0.85, 0.07, 0.07)
    n = 50_000
    ex_fern = fern.Ferns(parameters, distribution, n)
    x = ex_fern.iterate()

    coords_varia = Variations(x[:,0], -x[:,1], colors="g")
    variations = ["linear", "handkerchief", "swirl", "disc"]

    plt.figure(10, figsize=(9, 9))
    for i in range(4):
        plt.subplot(221 + i)
        variation = (variations[i])
        coords_varia.collection[variation]()
        coords_varia.plot()
        plt.title(variation)
    plt.show()


def example_transformation():
    """Plot of the Barnsely fern with linear combinations of variations.

    The linear combination gradually goes from linear -> swirl in 9 different
    combinations of the variations.
    """
    parameters = (
        (0, 0, 0, 0.16, 0, 0),
        (0.85, 0.04, -0.04, 0.85, 0, 1.60),
        (0.20, -0.26, 0.23, 0.22, 0, 1.60),
        (-0.15, 0.28, 0.26, 0.24, 0, 0.44),
    )
    distribution = (0.01, 0.85, 0.07, 0.07)
    n = 50_000
    ex_fern = fern.Ferns(parameters, distribution, n)
    x = ex_fern.iterate()

    N = 9
    sub = (np.sqrt(N)*110) + 1
    coeff = np.linspace(0, 1, N)
    coeffs = {}

    fern_varia = Variations(x[:,0], -x[:,1], colors="forestgreen")
    plt.figure(13, figsize=(9, 9))
    for i in range(N):
        plt.subplot(sub + i)
        coeffs["swirl"] = coeff[i]
        coeffs["linear"] = 1 - coeff[i]
        fern_varia(coeffs)
        fern_varia.plot()
    plt.show()




if __name__ == "__main__":
    example_solution()
    example_chaos()
    example_fern()
    example_transformation()
