import numpy as np
import matplotlib.pyplot as plt
import chaos_game as chaos
import fern as fern


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

      # private
        self._n = len(x)

    def __call__(self, coeffs):
        keys = list(coeffs)
        # import IPython; IPython.embed()
        self.collection[keys[1]]()
        u1 = self.u.copy()
        v1 = self.v.copy()
        self.collection[keys[0]]()
        u2 = self.u.copy()
        v2 = self.v.copy()
        self._u = u1*coeffs[keys[1]] + u2*coeffs[keys[0]]
        self._v = v1*coeffs[keys[1]] + v2*coeffs[keys[0]]
        # return self._u, self._v

   # private methods
    def _center(self):
        u = self._u
        v = self._v
        # import IPython; IPython.embed()
        x_median = np.mean(u)
        y_median = np.mean(v)
        self._u = u - x_median
        self._v = v - y_median

   # Properties
    @property
    def u(self):
        # print(f"max(_u):{max(self._u)}")
        # return self._u / self.scale
        # return self._u / max(self._u)
        return self._u

    @property
    def v(self):
        # return self._v / self.scale
        # print(f"max(_v):{max(self._v)}")
        # return self._v / max(self._v)
        return self._v
    
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
    def linear(self, center=False):
        self._u = self.x
        self._v = self.y
        if center:
            self._center()

    def handkerchief(self, center=False):
        r, theta = self.r, self.theta
        self._u = r * np.sin(theta + r)
        self._v = r * np.cos(theta - r)
        if center:
            self._center()

    def swirl(self, center=False):
        x, y = self.x, self.y
        r = self.r
        self._u = x * np.sin(r ** 2) - y * np.cos(r ** 2)
        self._v = x * np.cos(r ** 2) + y * np.sin(r ** 2)
        if center:
            self._center()

    def disc(self, center=False):
        theta, r = self.theta, self.r
        self._u = (theta / np.pi) * np.sin(np.pi * r)
        self._v = (theta / np.pi) * np.cos(np.pi * r)
        if center:
            self._center()

    # choose atleast two more to implement.
    def spherical(self, center=False):
        x, y = self.x, self.y
        r = self.r
        self._u = (1 / r ** 2) * x
        self._v = (1 / r ** 2) * y
        if center:
            self._center()

    def sinusoidal(self, center=False):
        x, y = self.x, self.y
        self._u = np.sin(x)
        self._v = np.sin(y)
        if center:
            self._center()

   # methods

    def plot(self, cmap=None):
        # fig, ax = plt.subplots()

        plt.scatter(self.u, -self.v, c=self.colors, cmap=cmap, s=0.1)
        # plt.ylim((-1.2, 1.2))
        # plt.xlim((-1.2, 1.2 ))
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
    grid_values = np.linspace(-1, 1, N - 5)
    test = chaos.ChaosGame(n=4, r=1 / 3)
    test.iterate(steps=N * N)
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

def example_weights():

    N = 200
    grid_values = np.linspace(-1, 1, N)
    parameters = (
        (0, 0, 0, 0.16, 0, 0),
        (0.85, 0.04, -0.04, 0.85, 0, 1.60),
        (0.20, -0.26, 0.23, 0.22, 0, 1.60),
        (-0.15, 0.28, 0.26, 0.24, 0, 0.44),
    )
    distribution = (0.01, 0.85, 0.07, 0.07)

    points = fern.ferns(parameters, distribution, N * N)

    N = 9
    sub = (np.sqrt(N)*110) + 1
    coeff = np.linspace(0, 1, N)
    coeffs = {}

    fern_varia = Variations(points[:,0], -points[:,1], colors="forestgreen")
    plt.figure(13, figsize=(9, 9))
    for i in range(N):
        plt.subplot(sub + i)
        coeffs["swirl"] = coeff[i]
        coeffs["linear"] = 1 - coeff[i]
        fern_varia(coeffs)
        fern_varia.plot()
    plt.show()


#not needed. 
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

# WRONG
def example_fern():
    N = 200
    grid_values = np.linspace(-1, 1, N)
    parameters = (
        (0, 0, 0, 0.16, 0, 0),
        (0.85, 0.04, -0.04, 0.85, 0, 1.60),
        (0.20, -0.26, 0.23, 0.22, 0, 1.60),
        (-0.15, 0.28, 0.26, 0.24, 0, 0.44),
    )
    distribution = (0.01, 0.85, 0.07, 0.07)

    points = fern.ferns(parameters, distribution, N * N)

    x_values = points[:,0]
    y_values = -points[:,1]


    coords_varia = Variations(x_values, y_values)

    variations = ["linear", "handkerchief", "swirl", "disc"]

    plt.figure(10, figsize=(9, 9))
    for i in range(4):
        plt.subplot(221 + i)
        # plot_grid()
        variation = variations[i]
        coords_varia.collection[variation](center=False)
        coords_varia.plot()
        plt.title(variation)
    plt.show()


if __name__ == "__main__":
    example_sulution()
    # example_chaos()
    example_fern()
    example_weights()
