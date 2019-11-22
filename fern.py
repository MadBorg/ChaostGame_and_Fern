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

    def transform(self, x, y):
        point = np.array((x, y))
        mat = np.matrix([[self.a, self.b], [self.c, self.d]])
        ef = np.array((self.e, self.f))

        start_point = np.dot(point, mat) + ef

        self.start_point = start_point

    def func_1(self, x):
        new_x = x[0] * 0
        new_y = x[1] * 0.16
        return np.array((new_x, new_y))

    def func_2(self, x):
        new_x = x[0] * 0.85 + x[1] * 0.04
        new_y = -x[0] * 0.04 + x[1] * 0.85 + 1.16
        return np.array((new_x, new_y))

    def func_3(self, x):
        new_x = x[0] * 0.2 - x[1] * 0.26
        new_y = x[0] * 0.23 + x[1] * 0.22 + 1.16
        return np.array((new_x, new_y))

    def func_4(self, x):
        new_x = -x[0] * 0.15 + x[1] * 0.28
        new_y = x[0] * 0.26 + x[1] * 0.24 + 0.44
        return np.array((new_x, new_y))

    def choose_func(self):
        p_val = np.array((0.01, 0.85, 0.07, 0.07))
        p_cumulative = np.cumsum(p_val)

        functions = [self.func_1, self.func_2, self.func_3, self.func_4]

        r = np.random.random()
        for j, p in enumerate(p_cumulative):
            if r < p:
                return functions[j]

    def iterate(self):
        point_list = np.zeros((50000, 2))
        point_list[0] = self.start_point

        for i in range(1, 50000):
            a = self.choose_func()
            point_list[i] = a(point_list[i - 1])

        self.point_list = point_list

    def plot_fern(self):
        plt.scatter(*zip(*self.point_list), marker=".", s=0.2, c="g")
        plt.axis("equal")
        plt.axis("off")
        plt.show()


if __name__ == "__main__":
    test = AffineTransform()
    test.transform(x=1, y=1)
    test.iterate()
