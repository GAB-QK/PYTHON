import matplotlib.pyplot as plt
import numpy as np

coord =np.array([[1, 3, 2, 1, 1, 3, 3],[3, 3, 5, 3, 1, 1, 3]])
print(coord[0],coord[1])
plt.plot(coord[0],coord[1])
'''
x = [1, 3, 2, 1, 1, 3, 3]
y = [3, 3, 5, 3, 1, 1, 3]
plt.plot(x, y)
plt.show()

'''


def rotation(angle):
    a = np.radians(angle)
    c = np.cos(a)
    s = np.sin(a)
    return np.array([[c, s], [-s, c]])


nouvelle_co = np.dot(rotation(90),coord)
plt.plot(nouvelle_co[0], nouvelle_co[1])

plt.show()

