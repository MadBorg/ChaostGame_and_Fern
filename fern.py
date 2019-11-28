import numpy as np
import matplotlib.pyplot as plt


class AffineTransform:
    """Class for a general affine transformation in the plane.

    Parameters
    -----------
    a, b, c, d, e, f: num, default: 0
    Free parameters for an affine transformation.
    """

    def __init__(self, a=0, b=0, c=0, d=0, e=0, f=0):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f

    def __call__(self, x, y):
        """Method for point (x,y) transformation into f(x,y)."""
        point = np.array((x, y))
        mat = np.array([[self.a, self.b], [self.c, self.d]], np.float)
        ef = np.array((self.e, self.f))

        return np.dot(mat, point) + ef

class Ferns:
    """A class for ferns.

    Parameters
    -----------
    p : (m*k) iterable float
        Parameters for different ferns instances.
    d : m iterable float
        The distribution of where the fern instances is going to be picked.
        sum(distribution) == 1
    n : int
        Number of iterations.
    x0 : (2) iterable
        Coordinates for starting point.
    """
    def __init__(self, p, d, n, x0=0):
        self.p = p
        self.d = d
        self.n = n
        self.x0 = x0

    def choose_func(self):
        """Generates n choices of functions derived from the cumulative distribution"""
        d_cumulative = np.cumsum(self.d)
        func_val = np.zeros(self.n, dtype="int")
        r = np.random.random(self.n)

        for i in range(self.n):
            for j, p in enumerate(d_cumulative):
                if r[i] < p:
                    func_val[i] = j
                    break
        return func_val

    def iterate(self):
        """Generates n coordinates (x, y).

        Notes
        ------
        The coordinate points depend on given parameters and the assigned
        probability of the functions.
        """
        p = self.p
        d = self.d
        n = self.n

        eps = 1e-13
        assert sum(d) - 1 < eps, f"sum(d) must equal 1, not {sum(d)}"
        assert len(p) == len(d), f"p and d must be of equal length: p:{len(p)}, d:{len(d)}"

        f = []
        for i in p:
            f.append(AffineTransform(a=i[0], b=i[1], c=i[2], d=i[3], e=i[4], f=i[5]))

        x = np.zeros((n, 2))
        x[0] = np.array(self.x0)
        func_val = self.choose_func()

        for i in range(1, n):
            x[i] = f[func_val[i]](x[i - 1, 0], x[i - 1, 1])

        return x


if __name__ == "__main__":
    parameters = (
        (0, 0, 0, 0.16, 0, 0),
        (0.85, 0.04, -0.04, 0.85, 0, 1.60),
        (0.20, -0.26, 0.23, 0.22, 0, 1.60),
        (-0.15, 0.28, 0.26, 0.24, 0, 0.44),
    )
    distribution = (0.01, 0.85, 0.07, 0.07)

    n = 100_000
    test = Ferns(parameters, distribution, n)
    x = test.iterate()

    plt.scatter(*zip(*x), marker=".", s=0.2, alpha=0.2, c="forestgreen")
    plt.axis("equal")
    plt.axis("off")
    plt.show()

    """
    Another one:
    parameters1 = (
        (0.44, 0.32, -0.07, 0.61, -0.001, -0.1),
        (-0.82, 0.16, -0.16, 0.81, -0.001, 4),
    )
    distribution1 = (0.3, 0.7)
    """
