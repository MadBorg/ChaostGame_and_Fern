import numpy as np
import matplotlib.pyplot as plt


class Triangle:
    def __init__(self, c0, c1, c2=None):
        """A class for making points inside an equilateral triangle.

        Parameters
        -----------
        c0, c1, c2 : arrays
            Coordinates (x,y) of corners of triangle.
        """
        self.c0 = c0
        self.c1 = c1

        if c2 is None:
            # rotating with rotation matrix
            diff = c1 - c0
            theta = 60 / 180 * np.pi
            rotation = np.array(
                ((np.cos(theta), np.sin(theta)), (np.sin(-theta), np.cos(theta)))
            )
            c2 = diff @ rotation

        self.c2 = c2

    def generate_point(self):
        """Generates starting point inside triangle."""
        self.c = self.c0, self.c1, self.c2
        w = np.random.random(3)
        w /= np.sum(w)

        return np.dot(w, self.c)

    def sierpinski_points(self, n):
        """Generates n points in sierpinski triangle.

        Returns
        ---------
        x: ndarray
            Coordinates (x, y) for points in sierpinski triangle.
        k : ndarray
            n x-corresponding values for which corner was used during iteration.
        """
        k = np.random.randint(3, size=n)
        x = np.zeros((n, 2))
        x[0] = self.generate_point()
        for i in range(1, n):
            x[i] = (x[i - 1] + self.c[k[i]]) / 2

        return x, k


def sierpinski_color_plot(x, k, color=("r", "g", "b")):
    """Plot of sierpinski triangle with 3 colors corresponding to k"""
    col1, col2, col3 = color
    col = np.where(k == 0, col1, np.where(k == 1, col2, col3))

    plt.scatter(*zip(*x[5:]), marker=".", s=0.2, c=col[5:])
    plt.axis("equal")
    plt.axis("off")
    plt.show()


def sierpinski_alt_colors(x, k, file_name=None):
    """Plot of sierpinski triangle using RGB colors dependent on k.

    Notes
    -------
    If a "file_name" is given, plot figure will be saved as file_name.
    """
    r = np.array(((1, 0, 0), (0, 1, 0), (0, 0, 1)))
    col = np.zeros((len(k), 3))
    col[0] = np.random.random(3)

    for i in range(1, len(k)):
        col[i] = (col[i - 1] + r[k[i]]) / 2

    fig, ax = plt.subplots()
    ax.scatter(*zip(*x[5:]), marker=".", s=0.2, c=col[5:])
    plt.axis("equal")
    plt.axis("off")
    if type(file_name) is str:
        fig.savefig(file_name)
    plt.show()


if __name__ == "__main__":

    n = 100_000
    tri = Triangle(np.array((0, 0)), np.array((1, 0)))
    x, k = tri.sierpinski_points(n)

    # sierpinski_color_plot(x, k)
    sierpinski_alt_colors(x, k)
