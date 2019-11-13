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
            (np.sin(-theta), np.cos(theta))
        ))
        c2 = diff @ rotation
    print(f"c0:{c0}, c1:{c1}, c2:{c2}")
    if plot:
        fig, ax = plt.subplots()
        ax.scatter(*zip(*(c0,c1,c2)))
        plt.show()
    return c0,c1,c2


def ex_b():
    n = 100000

    w = np.random.random(3)
    w /= np.sum(w)

    c = triangle(np.array((0,0)), np.array((1,0)))

    x = np.dot(w, c)
    x_points = np.zeros((n,2))
    x_points[0] = x

    k = np.random.randint(3, size=n)
    # color = np.empty(n)
    col = np.where(k==0, "r", np.where(k==1, "b", "g"))
    for i in range(1, n):
        x_points[i] = (x_points[i-1]+c[k[i]])/2

    plt.scatter(*zip(*x_points[5:]), marker= '.', s=0.1, color=col[5:])
    plt.axis('equal')
    plt.show()

def serpinski(n=10000):
    n = 100000

    w = np.random.random(3)
    w /= np.sum(w)

    c = triangle(np.array((0,0)), np.array((1,0)))

    x = np.dot(w, c)
    x_points = np.zeros((n,2))
    x_points[0] = x

    k = np.random.randint(3, size=n)

    for i in range(1, n):
        x_points[i] = (x_points[i-1]+c[k[i]])/2
    return x_points, k

def serpinski_color_plot(x, k, color=("r", "g", "b")):
    col1, col2, col3 = color
    col = np.where(k==0,col1 , np.where(k==1, col2, col3))

    plt.scatter(*zip(*x[5:]), marker= '.', s=0.1, color=col[5:])
    plt.axis('equal')
    plt.show()

def serpinski_alternative_colors(x,k):
    

if __name__ == "__main__":
    # c0, c1 = np.array((0,0)), np.array((1,0))
    # triangle(c0,c1, plot=True)
    x, k = serpinski()
    serpinski_color_plot(x,k)

