import numpy as np
import matplotlib.pyplot as plt
'''
axis: (x,y)
'''

def triangle(c0,c1,c2=None, plot=False):
    '''
        c0,c1,c2: numpy array
    '''
    if c2 is None:
        # rotating with rotation matrix
        diff = c1 - c0
        theta = 60/180*np.pi
        rotation = np.array((
            (np.cos(theta), np.sin(theta)),
            (np.cos(-theta), np.cos(theta))
        ))
        c2 = rotation @ diff
    print(f"c0:{c0}, c1:{c1}, c2:{c2}")
    if plot:
        fig, ax = plt.subplots()
        ax.scatter(*zip(*(c0,c1,c2)))
        plt.show()
    return c0,c1,c2

def test_triangle():
    c0,c1,c2 = np.array((0,0)), np.array((0,2)), np.array((1,1))

if __name__ == "__main__":
    c0, c1 = np.array((0,0)), np.array((1,0))
    triangle(c0,c1, plot=True)
        



