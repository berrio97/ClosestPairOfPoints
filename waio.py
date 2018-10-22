import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
"""puntos=[[2,5],[6,5],[7,1],[9,2],[10,5],[4,4],[2,7],[8,6],[3,4],[7,7]]
a = []
b = []
for i in puntos:
    a.append(i[0])
    b.append(i[1])
plt.plot(a, b, 'ro')
x=[6.5,0]
y=[6.5,4]
plt.plot([6.5,6.5], [0,10], 'k-', lw=2)
plt.show()"""



puntos=[[2,5,6],[6,5,0],[7,1,1],[9,2,5],[10,5,9],[4,4,8],[2,7,3],[8,6,10],[3,4,2],[7,7,5]]
xs = []
ys = []
zs = []
for i in puntos:
    xs.append(i[0])
    ys.append(i[1])
    zs.append(i[2])
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(6.5,0,0)

ax.scatter(xs, ys, zs)

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
plt.show()