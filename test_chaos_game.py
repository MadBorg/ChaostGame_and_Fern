import numpy as np
import matplotlib.pyplot as plt
import numpy.testing as npt
from chaos_game import ChaosGame

def test_init_values():
    wrong_n = 3.8
    wrong_r = 5

    with npt.assert_raises(ValueError):
        test = ChaosGame(n=wrong_n, r=wrong_r)


if __name__ == "__main__":

    test_init_values()
