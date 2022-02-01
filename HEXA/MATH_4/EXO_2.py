import numpy as np

m = np.array([[0, 0, 1, 0, 0], [0, 1, 1, 1, 0], [0, 1, 0, 0, 0], [0, 0, 0, 0, 1], [1, 1, 0, 0, 1]])
p = np.array([[0, 0, 1, 0, 0], [0, 1, 1, 1, 0], [0, 1, 0, 0, 0], [0, 0, 0, 0, 1], [1, 1, 0, 0, 1]])
i = 1
while m[0:4] == 0:
    p = np.dot(p, m)
    i += 1
print("chemin de longueur", i)
print(p)
