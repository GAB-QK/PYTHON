import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

fig = plt.figure()
ax = fig.add_subplot()
T = True

xy=(0,0)
w=4
h=2

rect = Rectangle(xy, w, h, color="gray")


w = w*2
h = h*2
rectangle = Rectangle((4,2), w, h, outline="blue")

ax.add_patch(rect)
ax.add_patch(rectangle)


plt.axis('equal')

plt.show()