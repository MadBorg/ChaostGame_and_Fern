import numpy as np
# import matplotlib.pyplot as plt


class Variations:
    """
    Altrering coordinates.
    So if you have a set of coordinates it alters them in a specific way..
    """

    def __init__(self, x, y, colors="black"):
       # dock

       # asserts
        try:
            iter(x)
        except:
            raise TypeError("x is not an iterable")
        try:
            iter(y)
        except:
            raise TypeError("y is not an iterable")

      # selfs
       # change dtype
        if type(x) != np.ndarray:
            self.x = np.array(x, dtype="float_")
        else:
            self.x = x
        if type(y) != np.ndarray:
            self.y = np.array(y, dtype="float_")
        else:
            self.y = y

       # standard
        self.colors = colors

       # private
        self._n = len(x)
        self._u = x
        self._v = y
   # Properties
    @property
    def r(self):
        return np.sqrt(self.x**2 + self.y**2)

    @property
    def theta(self):
        return np.arctan2(self.x, self.y)

    @property
    def phi(self):
        return np.arctan2(self.y, self.x)

   # Variations
    def linear(self):
        self._u = self._u
        self._v = self._v

    def handkerchief(self):
        self._u = r * sin()

    def swirl(self):
        pass

    def disc(self):
        pass

    # choose atleast two more to implement.
    def fun1(self):
        pass

    def fun2(self):
        pass
