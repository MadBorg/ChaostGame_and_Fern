import numpy as np
# import matplotlib.pyplot as plt


class Variations:
    """
    Altrering coordinates.
    So if you have a set of coordinates it alters them in a specific way..
    """
    variations = ["linear", "handkerchief", "swirl", "disc", "spherical", "sinusoidal"]
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

    @property
    def u(self):
        return self._u
    
    @property
    def v(self):
        return self._v

   # Variations
    def linear(self):
        self._u = self._u
        self._v = self._v

    def handkerchief(self):
        r, theta = self.r, self.theta
        self._u = r * np.sin(theta + r)
        self._v = r * np.cos(theta - r)

    def swirl(self):
        x, y =self.x, self.y
        r = self.r
        self._u = x*np.sin(r**2) - y*np.cos(r**2)
        self._v = x*np.cos(r**2) + y*np.sin(r**2)

    def disc(self):
        theta, r = self.theta, self.r
        self._u = (theta/np.pi) * np.sin(np.pi * r)
        self._v = (theta/np.pi) * np.cos(np.pi * r)
    # choose atleast two more to implement.
    def spherical(self):
        x, y = self.x, self.y
        r = self.r
        self._u = (1/r**2) * x
        self._v = (1/r**2) * y

    def sinusoidal(self):
        x, y = self.x, self.y
        self._u = np.sin(x)
        self._v = np.sin(y)
