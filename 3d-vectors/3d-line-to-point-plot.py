from mpl_toolkits import mplot3d
import matplotlib.pyplot as plot

figure = plot.figure()
axes = plot.axes(projection='3d')

axes.scatter3D(10, 10, 10, c=10)

VecStart_x = [0]
VecStart_y = [0]
VecStart_z = [0]
VecEnd_x = [10]
VecEnd_y = [10]
VecEnd_z = [10]
for i in range(1):
    axes.plot([VecStart_x[i], VecEnd_x[i]], [VecStart_y[i],
                                           VecEnd_y[i]], zs=[VecStart_z[i], VecEnd_z[i]])
plot.show()
