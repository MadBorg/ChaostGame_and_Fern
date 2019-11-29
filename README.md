# Oblig3 IN1910

## triangle.py
    triangle(np.array,np.array,np.array=None,boolean=False):
        args, kwards:
        ---
            c0: numpy array
                first point in the triangle
            c1: nupy array
                second point in the triangle
            c2: nupy array = None
                thrd point in the triangle or None.
            plot: boolean
                if plot then plot
        Code
        ---
            if c2 is None
                using a rotation matrix to rotate the difference between c1 and c0 60 degrees. That way we get a equilateral triangle.
            if plot:
                plots the 3 points in the triangle.

        Returns
        ----
            np.array,np.array,np.array

    serpinski(n=10_000):
        args:
        ---
            n: int
                number of points in the triangle.
        Code:
        ---
            c: the 3 points from the triangle
            w: random weights used to calculate the start point.
            x: startpoint from the weight w and triangle c
            k: a numpy array of lenght n of random ints to pick a random corner of the triangle c.
            x_points: is a (n, 2) matix(list of coordinates) where index 0 is the random start point x. And the rest is calculated from the diference equation x_n = (x_n-1 + c_k_i) / 2. where k_i is a random index to pick a random corner from c.
        Return:
        ---
        x_points: numpy array<float>
            shape:(n,2)
        k: numpy array<int>
            shape:(3, n)

## Part A)
## Part B)
## Part C)
## Part D)
