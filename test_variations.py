import numpy as np
import variations

def test_variatons_init_coordinates_shape():
    n = 1e5
    x = np.linspace(-10,100,n)
    y = np.linspace(-10,100,n)*2
    test = variations.Variations(x,y)
    assert x.shape == (n,) , f"x.shape should be ({n},), but it is {x.shape}."
    assert y.shape == (n,) , f"y.shape should be ({n},), but it is {y.shape}."

def test_variatons_init_dtypes():
    n = 1e5
    x = np.linspace(-10,100,n)
    y = np.linspace(-10,100,n)*2
    # x, y= [1], [2]
    test = variations.Variations(x,y)
    if type(test.x) != np.ndarray:
        raise ValueError(f"x is not an np.ndarray, it is {type(test.x)}")
    if type(test.y) != np.ndarray:
        raise ValueError(f"y is not an np.ndarray, it is {type(test.y)}")

if __name__ == "__main__":
    test_variatons_init_coordinates_shape()
    test_variatons_init_dtypes()