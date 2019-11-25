import numpy as np
import matplotlib.pyplot as plt

class AffineTransform():

    def __init__(self, a=0, b=0, c=0, d=0, e=0, f=0):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f

    def __call__(self, x, y):
        point = np.array((x, y))
        mat = np.array([[self.a, self.b],[self.c, self.d]],np.float)
        ef = np.array((self.e, self.f))

        new_point = np.dot(mat,point) + ef
        self.new_point = new_point
        return new_point

 
def cumChoice(d, n):
    """
    Params:
    ----
    d np.array(mxn)<float>
        Distribution for the cumulative distributions
    n int
        number for choices
    Returns:
    ----
    choices
        n Choises derrived from the distribution
    """
    r = np.random.random(n)
    d_cumulative = np.cumsum(d)
    choices = np.zeros(n, dtype="int")

    for i in range(n):
        for j, d in enumerate(d_cumulative):
            if r[i] < d:
                choices[i] = j
                break
    return choices

def ferns(parameters, distribution, n, x0=0):
    """
    Params:
    ----
    parameters: (m * k) iterable float
        Parameters for the different fern instances
    distribution: (m) iterable float
        The distribution of where the fern instances is going to be picked.
        sum(distribution) == 1
    x0: (2) iterable
        starting point
    Returns:
    ----
    x (n,2) np.array
        coordinate points

    """
    eps = 1e-13
    assert sum(distribution) - 1 < eps, f"sum(distribution must be 1) it is {sum(distribution)}"
    assert len(parameters) == len(distribution), f"lenth of parameters must be equal to lenght of distribution: len(parameters):{len(parameters)}, len(distribution):{len(distribution)}"
    # import IPython; IPython.embed()

    f = []
    for i in parameters:
        # print(f"\n i:{i}")
        f.append(AffineTransform(a=i[0], b=i[1],c=i[2],d=i[3],e=i[4],f=i[5]))
    x = np.zeros((n,2))
    x[0] = x0
    choices = cumChoice(distribution, n)
    for i in range(0, len(choices)):
        # print(f"x[i]:{x[i]}, *zip(z[i]):{x[i]))}")
        x[i] = f[choices[i]](x[i-1, 0], x[i-1, 1])
    return x

def fun(x,y):
    return (x,y)   
if __name__ == '__main__':
    parameters= (
        (    0,    0,    0, 0.16,   0,    0),
        ( 0.85, 0.04,-0.04, 0.85,   0, 1.60),
        ( 0.20,-0.26, 0.23, 0.22,   0, 1.60),
        (-0.15,0.28 , 0.26, 0.24,   0, 0.44)
    )
    distribution=(0.01, 0.85, 0.07, 0.07)
    n = 50_000
    points = ferns(parameters, distribution, n)
    plt.scatter(*zip(*points), marker=".", s=0.2, alpha=0.2, c="g")
    plt.show()

    # test = AffineTransform()
    # test.transform(x=1, y=1)
    # test.func_1()
    # test.func_2()
    # test.func_3()
    # test.func_4()
