import matplotlib.pyplot as plt
import numpy as np

a = np.array([2, 5, 4, 1])
print(a)

b = np.array([1, -2, 0, 2])
print(b)

print(a + b)

grille = np.array([[2, 4], [0, 3], [5, 1]])
print("grille", grille)
print("grille+1", grille + 1)

grille2 = np.array([[[2, 4], [0, 3], [5, 1]], [[2, 4], [0, 3], [5, 1]]])

print(grille.ndim)  # donne la dimension de array
print(grille2.ndim)
print(a.ndim)

print(grille.shape)
print(a.shape)

grille3 = np.array([[2, 6, 3], [1, 0, 8], [-6, 4, 4], [0, -1, 1]])
print("")
print(grille3)
print(grille3.ndim)
print(grille3.shape)  # 4*3

grille3D = np.array([[[2, 6], [1, 0], [3, 0]], [[7, 9], [-6, 4], [0, -1]]])
print("")
print(grille3D)
print(grille3D.ndim)
print(grille3D.shape)

print(grille3D[0])
print(grille3D[0, 0])
print(grille3D[0, 0, 0])

print("")
c = np.arange(3, 12, 2)
print(c)
# linspace ( debut, fin, nombre)
d = np.linspace(4, 6, 9)
print(d)


def f(x):
    return x ** 3 - 4 * x ** 2 + 10 * x - 20


x = np.linspace(-5, 5, 100)
plt.plot(x, f(x))

# exemple trajectoiree
t = np.linspace(0, 10, 15)
plt.plot(3 * t, t ** 2)
plt.show()
# créer des arrays multidimensionels
z = np.zeros((5, 3))
print(z)

print("")
identite = np.eye(4)
print(identite)
print(identite.shape)
print("")


D = np.eye(5)
print(3*D+4)


