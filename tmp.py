import numpy as np
import matplotlib.pyplot as plt

ax = 0
ay = 0
A = (ax,ay)

bx = 1
by = 0
B = (bx, by)

dx = (bx+ax)/2
dy = (by+ay)/2
D = (dx, dy)

cx = (ax + bx)/2
cy = np.sqrt(((ax+bx)/2)**2 - ((ax+dx)/2)**2)
C = (cx,cy)

print(f"A:{A}, B:{B}, C:{C}")
plt.scatter(A,B,C)
plt.show()

