import numpy as np
import variations


def test_variatons_init_coordinates_shape():
    n = 1e5
    x = np.linspace(-10, 100, n)
    y = np.linspace(-10, 100, n)
    test = variations.Variations(x, y)
    assert x.shape == (n,), f"x.shape should be ({n},), but it is {x.shape}."
    assert y.shape == (n,), f"y.shape should be ({n},), but it is {y.shape}."


def test_variatons_init_dtypes():
    n = 1e5
    x = np.linspace(-10, 100, n)
    y = np.linspace(-10, 100, n)*2
    # x, y= [1], [2]
    test = variations.Variations(x, y)
    if type(test.x) != np.ndarray:
        raise ValueError(f"x is not an np.ndarray, it is {type(test.x)}")
    if type(test.y) != np.ndarray:
        raise ValueError(f"y is not an np.ndarray, it is {type(test.y)}")


def test_variatons_r():
    x = (0, 0, 1, 2,          1,                   4)
    y = (0, 1, 0, 0,          1,                   3)
    r = (0, 1, 1, 2, np.sqrt(2), np.sqrt(4**2 + 3**2))
    # r = (0, 0, 0, 0,          0,                   0)
    x,y,r = np.array(x), np.array(y), np.array(r)
    test = variations.Variations(x, y)
    eps = 1e-13
    # import IPython; IPython.embed()
    assert np.all(abs(test.r - r) < eps), "test_variatons_r failed over: np.all(abs(test.r - r) < eps)"

def test_variatons_theta():
    x = np.linspace(1, 100, 200)
    y = np.linspace(1, 100, 200)
    np.random.shuffle(y)
    test = variations.Variations(x, y)
    eps = 1e-10
    # import IPython; IPython.embed()
    # using that tan( arctan x ) = x to test theta
    assert np.all(abs(x/y - np.tan(test.theta)) < eps), "test_variatons_theta failed over: np.all(abs(x/y - np.tan(test.theta)) < eps)"

def test_variatons_phi():
    x = np.linspace(1, 100, 200)
    y = np.linspace(1, 100, 200)
    np.random.shuffle(y)
    test = variations.Variations(x, y)
    eps = 1e-10
    # import IPython; IPython.embed()
    # using that tan( arctan x ) = x to test theta
    assert np.all(abs(y/x - np.tan(test.phi)) < eps), "test_variatons_r failed over: np.all(abs(y/x - np.phi(test.theta)) < eps)"


def test_variatons_linear():
    n = 1e5
    x = np.linspace(-10, 100, n)*3
    y = np.linspace(-10, 100, n)*2
    test = variations.Variations(x, y)
    test.linear()
    eps = 1e-14
    # test._u *= 10
    # test._v *= 10
    assert np.all(abs(test._u - x) < eps), "linear changed the x values"
    assert np.all(abs(test._v - y) < eps), "linear changed the y values"

def test_variatons_handkerchief():
    n = 1e3
    x = np.linspace(0.1, 1, n)
    y = np.linspace(0.1, 1, n)
    np.random.shuffle(y)
    test = variations.Variations(x, y)
    test.handkerchief()
    r, theta = test.r, test.theta
    x_test = np.arcsin(test._u/r) - r
    y_test = np.arccos(test._v/r) + r
    eps = 1e-14
    import IPython; IPython.embed()
    assert np.all(abs(test._u - x) < eps), "linear changed the x values"
    assert np.all(abs(test._v - y) < eps), "linear changed the y values"

# def test_variatons_init_color():
#     #test if color exist

# TODO: Test your implementation by comparing plots of variations of a uniformly spaced grid $x, y \in [-1, 1]$ with the figures in the Catalog of Variations. Note that you cannot use meshgrid to generate the grid, as the grid must be represented as two one dimensional arrays containing $x$-values and $y$-values. Let the size of the grid be $60 \times 60$ coordinates(i.e. x and y should be arrays of length 3600).
if __name__ == "__main__":
    test_variatons_init_coordinates_shape()
    test_variatons_init_dtypes()
    test_variatons_linear()
    # test_variatons_handkerchief()
    test_variatons_r()
    test_variatons_theta()
    test_variatons_phi()