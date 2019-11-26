import numpy as np
import matplotlib.pyplot as plt

class AffineTransform:
    def __init__(self, a=0, b=0, c=0, d=0, e=0, f=0):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f

    def __call__(self, x, y):
        point = np.array((x, y))
        mat = np.array([[self.a, self.b], [self.c, self.d]], np.float)
        ef = np.array((self.e, self.f))

        new_point = np.dot(mat, point) + ef
        self.new_point = new_point
        return new_point

class Fern:
   # special methods
    def __init__(self, parameters, distribution, n):
        """
        Params:
        ----
        d np.array(mxn)<float>
            Distribution for the cumulative distributions
        n int
            number for choices
        """
        self.distribution = distribution
        self.parameters = parameters
        self.n = n

    def __call__(self, x0=0, eps=1e-13):
        self.iterate(x0, eps)
        return self.points
        

   # properties
    @property
    def x(self):
        return self.points[:,1]
    @property
    def y(self):
        return self.points[:,1]
    @property
    def points(self):
        return self._points

   # methods
    def _cumChoice(self):
        n = self.n
        d = self.distribution
        r = np.random.random(n)
        d_cumulative = np.cumsum(d)
        choices = np.zeros(n, dtype="int")

        for i in range(n):
            for j, d in enumerate(d_cumulative):
                if r[i] < d:
                    choices[i] = j
                    break
        self.choices = choices
        return choices


    def iterate(self, x0=0, eps=1e-13):
        #args
        parameters, distribution, n = self.parameters, self.distribution, self.n
        #tests
        assert (
            sum(distribution) - 1 < eps
        ), f"sum(distribution must be 1) it is {sum(distribution)}"
        assert len(parameters) == len(distribution), f"length of parameters must be equal to lenght of distribution: len(parameters):{len(parameters)}, len(distribution):{len(distribution)}"
        #function
        f = []
        for i in parameters:
            # print(f"\n i:{i}")
            f.append(AffineTransform(a=i[0], b=i[1], c=i[2], d=i[3], e=i[4], f=i[5]))
        x = np.zeros((n,2))
        x[0] = x0
        choices = self._cumChoice()
        for i in range(0, len(choices)):
            x[i] = f[choices[i]](x[i - 1, 0], x[i - 1, 1])
        # end
        self._points = x
             
if __name__ == "__main__":
    parameters = (
        (0, 0, 0, 0.16, 0, 0),
        (0.85, 0.04, -0.04, 0.85, 0, 1.60),
        (0.20, -0.26, 0.23, 0.22, 0, 1.60),
        (-0.15, 0.28, 0.26, 0.24, 0, 0.44)
    )
    distribution = (0.01, 0.85, 0.07, 0.07)
    n = 50_000
    test = Fern(parameters, distribution, n)
    test.iterate()
    plt.scatter(*zip(*test.points), marker=".", s=0.2, alpha=0.2, c="g")
    plt.axis("equal")
    plt.axis("off")
    plt.show()
