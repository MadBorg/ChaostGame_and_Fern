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
        # print(f"\n\n x:{x}, y:{y}\n\n")
        point = np.array((x, y))
        mat = np.array([[self.a, self.b],[self.c, self.d]],np.float)
        ef = np.array((self.e, self.f))
        # import IPython; IPython.embed()
        # new_point = (np.cross(point,mat) + ef)

        # print(f"\nmat:{mat}, point:{point}")
        # print(f"dot:{np.dot(mat,point)}, ef:{ef}\n")

        new_point = np.dot(point, mat) + ef

        # print(f"\nnew_point:{new_point}\n")
        self.new_point = new_point
        return new_point
#
    # def transform(self, x, y):
    #     point = np.array((x, y))
    #     mat = np.matrix([[self.a, self.b], [self.c, self.d]])
    #     ef = np.array((self.e, self.f))

    #     start_point = (np.dot(point, mat) + ef)

    #     self.start_point = start_point


    # def func_1(self, steps=10):

    #     n_p = np.zeros((steps, 2))
    #     n_p[0] = self.start_point

    #     for i in range(1, steps):
    #         n_p[i, 0] = n_p[i-1,0]*0
    #         n_p[i, 1] = n_p[i-1,1]*0.16


    # def func_2(self, steps=10):

    #     n_p = np.zeros((steps, 2))
    #     n_p[0] = self.start_point

    #     for i in range(1, steps):
    #         n_p[i, 0] = n_p[i-1,0]*0.85 + n_p[i-1,1]*0.04
    #         n_p[i, 1] = -n_p[i-1,0]*0.04 + n_p[i-1,1]*0.85 + 1.16


    # def func_3(self, steps=10):

    #     n_p = np.zeros((steps, 2))
    #     n_p[0] = self.start_point

    #     for i in range(1, steps):
    #         n_p[i, 0] = n_p[i-1,0]*0.2 - n_p[i-1,1]*0.26
    #         n_p[i, 1] = n_p[i-1,0]*0.23 + n_p[i-1,1]*0.22 + 1.16

    # def func_4(self, steps=10):

    #     n_p = np.zeros((steps, 2))
    #     n_p[0] = self.start_point

    #     for i in range(1, steps):
    #         n_p[i, 0] = -n_p[i-1,0]*0.15 + n_p[i-1,1]*0.28
    #         n_p[i, 1] = n_p[i-1,0]*0.26 + n_p[i-1,1]*0.24 + 0.44

 
def cumChoice(p, n):
    r = np.random.random(n)
    p_cumulative = np.cumsum(p)
    choices = np.zeros(n, dtype="int")

    for i in range(n):
        for j, p in enumerate(p_cumulative):
            if r[i] < p:
                choices[i] = j
                break
    return choices


def ferns(parameters, distribution, n, x0=0):
    f = []
    for i in parameters:
        f.append(AffineTransform(*i))
    x = np.zeros((n,2))
    x[0] = x0
    choices = cumChoice(distribution, n)
    for i in range(0, len(choices)):
        # print(f"\nx[i-1]:{x[i-1]}\n")
        x[i] = f[choices[i]](x[i-1][0],x[i-1][1])
        # print(x[i-1])
        # x[i] = f[choices[i]](*zip(x[i-1]))

    return x

    



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
    plt.scatter(*zip(*points), marker=".", s=0.2, alpha=0.2)
    plt.show()

    # test = AffineTransform()
    # test.transform(x=1, y=1)
    # test.func_1()
    # test.func_2()
    # test.func_3()
    # test.func_4()
