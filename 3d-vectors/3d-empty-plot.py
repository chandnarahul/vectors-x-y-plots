from mpl_toolkits import mplot3d
import matplotlib.pyplot as plot

figure = plot.figure()
axes = plot.axes(projection='3d')

VecStart_x = [00,00, 00,00, 00,00,00]
VecStart_y = [00,00, 00,00, 00,00,00]
VecStart_z = [10,10, 10,10, 10,00,20]
VecEnd_x =   [00,10,-10,00, 00,00,00]
VecEnd_y =   [00,00, 00,10,-10,00,00]
VecEnd_z =   [10,10, 10,10, 10,10,10]
for i in range(7):
    axes.scatter3D(VecEnd_x[i], VecEnd_y[i], VecStart_z[i], c=10)
    axes.plot([VecStart_x[i], VecEnd_x[i]], [VecStart_y[i],
                                           VecEnd_y[i]], zs=[VecStart_z[i], VecEnd_z[i]])
plot.show()
