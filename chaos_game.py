import numpy as np
import matplotlib.pyplot as plt


class ChaosGame():
    """A class for a chaos game.

    Parameters
    -----------
    n : int, default: 3
        Number of sides in n-gon.
    r : float, default: 1/2
        Ratio between two points.
    """

    def __init__(self, n=3, r=1/2):
        self.n = n
        self.r = r
        self._generate_ngon()

        if type(n) != int:
            raise ValueError("n must be an integer")
        if not 0 < r < 1:
            raise ValueError("r must be on (0,1) interval")


    def _generate_ngon(self):
        n = self.n
        theta = np.linspace(0, 2*np.pi, n+1)
        c = np.zeros((n, 2))

        for i in range(n):
            c[i] = (np.sin(theta[i]), np.cos(theta[i]))

        self.c = c

    def plot_ngon(self):
        plt.scatter(*zip(*self.c))
        plt.axis('equal')
        plt.show()


    def _starting_point(self):
        n = self.n
        w = np.random.random(n)
        w /= np.sum(w)
        x = np.dot(w, self.c)

        return x

    def iterate(self, steps=100000, discard=5):
        r = self.r
        c = self.c
        k = np.random.randint(self.n, size=steps)

        y = np.zeros((steps, 2))
        y[0] = self._starting_point()

        for i in range(1, steps):
            y[i] = (r*y[i-1]) + ((1-r)*c[k[i]])

        return y

    def plot(self, color=False, cmap='jet'):
        new = self.iterate()

        plt.scatter(*zip(*new[5:]), marker= '.', s=0.2)
        plt.axis('equal')
        plt.show()



if __name__ == "__main__":

    #for i in range(3, 9):
        #test = ChaosGame(i)
        #test.plot_ngon()

    test = ChaosGame(n=8, r=1/100)
    test.plot()
