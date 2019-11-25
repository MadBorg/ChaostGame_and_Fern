import numpy as np
import variations


def test_variatons_init_coordinates_shape():
    n = 1e5
    x = np.linspace(-10, 100, n)
    y = np.linspace(-10, 100, n)*2
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

# def test_variatons_init_color():
#     #test if color exist

def test_variatons_linear():
    n = 1e5
    x = np.linspace(-10, 100, n)*3
    y = np.linspace(-10, 100, n)*2
    test = variations.Variations(x, y)
    test.linear()
    eps = 1e-14
    assert all(test._u - x) < eps, "linear changed the x values"
    assert all(test._v - y) < eps, "linear changed the y values"


if __name__ == "__main__":
    test_variatons_init_coordinates_shape()
    test_variatons_init_dtypes()
