import numpy as np
import matplotlib.pyplot as plt
import numpy.testing as npt
from chaos_game import ChaosGame

def test_init_values():
    wrong_n = 3.8
    wrong_r = 5

    with npt.assert_raises(ValueError):
        test = ChaosGame(n=wrong_n, r=wrong_r)

def test_called_iterate():
    test = ChaosGame()

    with npt.assert_raises(AttributeError):
        test.show()

def test_big_y():
    test = ChaosGame(4, 1/2)
    test.iterate(10_000)
    points = test.x
    assert points.any() <= 1, "not all points y is smaller then one"
        
def negative_n():
    n = -4
    with npt.assert_raises(ValueError):
        ChaosGame(n, 1/2)


if __name__ == "__main__":

    test_init_values()
    test_called_iterate()
    test_big_y()
    negative_n()
