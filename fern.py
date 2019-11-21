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


    def transform(self, x, y):
        point = np.array((x, y))
        mat = np.matrix([[self.a, self.b], [self.c, self.d]])
        ef = np.array((self.e, self.f))

        start_point = (np.dot(point, mat) + ef)

        self.start_point = start_point


    def func_1(self, steps=10):

        n_p = np.zeros((steps, 2))
        n_p[0] = self.start_point

        for i in range(1, steps):
            n_p[i, 0] = n_p[i-1,0]*0
            n_p[i, 1] = n_p[i-1,1]*0.16


    def func_2(self, steps=10):

        n_p = np.zeros((steps, 2))
        n_p[0] = self.start_point

        for i in range(1, steps):
            n_p[i, 0] = n_p[i-1,0]*0.85 + n_p[i-1,1]*0.04
            n_p[i, 1] = -n_p[i-1,0]*0.04 + n_p[i-1,1]*0.85 + 1.16


    def func_3(self, steps=10):

        n_p = np.zeros((steps, 2))
        n_p[0] = self.start_point

        for i in range(1, steps):
            n_p[i, 0] = n_p[i-1,0]*0.2 - n_p[i-1,1]*0.26
            n_p[i, 1] = n_p[i-1,0]*0.23 + n_p[i-1,1]*0.22 + 1.16

    def func_4(self, steps=10):

        n_p = np.zeros((steps, 2))
        n_p[0] = self.start_point

        for i in range(1, steps):
            n_p[i, 0] = -n_p[i-1,0]*0.15 + n_p[i-1,1]*0.28
            n_p[i, 1] = n_p[i-1,0]*0.26 + n_p[i-1,1]*0.24 + 0.44




if __name__ == '__main__':
    test = AffineTransform()
    test.transform(x=1, y=1)
    test.func_1()
    test.func_2()
    test.func_3()
    test.func_4()
