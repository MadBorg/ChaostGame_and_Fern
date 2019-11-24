import numpy as np
import matplotlib.pyplot as plt
import triangle as t
# ax = 0
# ay = 0
# A = (ax,ay)

# bx = 1
# by = 0
# B = (bx, by)

# dx = (bx+ax)/2
# dy = (by+ay)/2
# D = (dx, dy)

# cx = (ax + bx)/2
# cy = np.sqrt(((ax+bx)/2)**2 - ((ax+dx)/2)**2)
# C = (cx,cy)

# print(f"A:{A}, B:{B}, C:{C}")
# plt.scatter(*zip(A,B,C))
# plt.show()
x_points = np.zeros((50,2))

i = np.random.randint(3, size=50)

c = t.triangle((0,0,))

