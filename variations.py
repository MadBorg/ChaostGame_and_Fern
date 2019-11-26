import numpy as np
import matplotlib.pyplot as plt
import chaos_game as chaos


class Variations:
    """
    Altrering coordinates.
    So if you have a set of coordinates it alters them in a specific way..
    """

    def __init__(self, x, y, colors="black"):
       # dock

       # asserts
        try:
            iter(x)
        except:
            raise TypeError("x is not an iterable")
        try:
            iter(y)
        except:
            raise TypeError("y is not an iterable")

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

      # private
        self._n = len(x)
        self._u = x
        self._v = y

   # Properties
    @property
    def r(self):
        return np.sqrt(self.x ** 2 + self.y ** 2)

    @property
    def theta(self):
        return np.arctan2(self.x, self.y)

    @property
    def phi(self):
        return np.arctan2(self.y, self.x)

    @property
    def u(self):
        return self._u

    @property
    def v(self):
        return self._v

   # Variations
    def linear(self):
        self._u = self._u
        self._v = self._v

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

    # methods

    def plot(self, cmap=None):
        # fig, ax = plt.subplots()

        plt.scatter(self.u, -self.v, c=self.colors, cmap=cmap, s=0.1)
        plt.axis("equal")
        plt.axis("off")


def plot_grid():
    plt.plot([-1, 1, 1, -1, -1], [-1, -1, 1, 1, -1], color="grey")
    plt.plot([-1, 1], [0, 0], color="grey")
    plt.plot([0, 0], [-1, 1], color="grey")


def example_sulution():
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
    N = 300
    grid_values = np.linspace(-1, 1, N-5)
    test = chaos.ChaosGame(n=4, r=1/3)
    test.iterate(steps=N*N)
    x_values = test.x_points
    y_values = test.y_points

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

def example_general(cls=None, N=300, **kwargs):
    """
    Params:
    ----
    cls: class
        a class that gives coordinates via a iterate method and have the properties x_values and y_values
    N: int
        sqrt of number of iterations
    **kwargs:
        keywordarguments for the class

    """
    if cls is None:
        example_sulution()
        return 0
    grid_values = np.linspace(-1, 1, N-5)
    test = cls(**kwargs)
    test.iterate(steps=N*N)
    x_values = test.x_points
    y_values = test.y_points

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



if __name__ == "__main__":
    # example_sulution()
    # example_chaos()
    example_general(chaos.ChaosGame, n=6, r=1/5)
