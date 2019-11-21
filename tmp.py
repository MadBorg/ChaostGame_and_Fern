import numpy as np
import matplotlib.pyplot as plt
import triangle as t
# ax = 0
# ay = 0
# A = (ax,ay)

# bx = 1
# by = 0
# B = (bx, by)

# dx = (bx+ax)/2
# dy = (by+ay)/2
# D = (dx, dy)

# cx = (ax + bx)/2
# cy = np.sqrt(((ax+bx)/2)**2 - ((ax+dx)/2)**2)
# C = (cx,cy)

# print(f"A:{A}, B:{B}, C:{C}")
# plt.scatter(*zip(A,B,C))
# plt.show()
x_points = np.zeros((50,2))

i = np.random.randint(3, size=50)

c = t.triangle((0,0,))

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