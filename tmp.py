import numpy as np
import matplotlib.pyplot as plt
import timeit

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
        c[:, 0] = np.sin(theta[:-1])
        c[:, 1] = np.cos(theta[:-1])
        # for i in range(n):
        #     c[i] = (np.sin(theta[i]), np.cos(theta[i]))

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

    def iterate(self, steps=100_000, discard=5):
        r = self.r
        c = self.c
        k = np.random.randint(self.n, size=steps)

        y = np.zeros((steps, 2))
        y[0] = self._starting_point()

        for i in range(1, steps):
            y[i] = (r*y[i-1]) + ((1-r)*c[k[i]])
        self.k = k[discard:]
        return y[discard:]

    def plot(self, color=False, cmap='jet'):
        new = self.iterate()
        fig, ax = plt.subplots()
        if color:
            k = self.k
            # colors = np.where(k==0,col1 , np.where(k==1, col2, col3))
            colors = k
            ax.scatter(*zip(*new), marker= '.', s=0.2, c=colors, cmap=cmap)
        else:
            ax.scatter(*zip(*new), marker= '.', s=0.2)
        ax.axis('equal')
        return fig, ax

    def show(self, color=False, cmap='jet'):
        fig, ax = self.plot(color, cmap)
        fig.show()



def check_plot():
    g = ChaosGame(3,1/2)
    g.show(color=True)
    # g.show(color=True)

if __name__ == "__main__":

    #for i in range(3, 9):
        #test = ChaosGame(i)
        #test.plot_ngon()

    # test = ChaosGame(n=int(1e5), r=1/5)
    # test.plot()
    # print(timeit.timeit("x = ChaosGame(n=int(1e3), r=1/5); x.plot(show=False)", setup="from __main__ import ChaosGame", number=100))

    check_plot()