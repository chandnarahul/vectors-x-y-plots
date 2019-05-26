from mpl_toolkits import mplot3d
import matplotlib.pyplot as plot

figure = plot.figure()
axes = plot.axes(projection='3d')

VecStart_x = [0,0,0 ,00,00,00,00,00,00,00,00]
VecStart_y = [0,0,0 ,00,00,00,00,00,00,00,00]
VecStart_z = [0,0,0 ,00,00,00,00,00,00,00,00]
VecEnd_x = [10,20,20,20,20,20,20,20,20,20,20]
VecEnd_y = [10,20,20,20,20,20,20,20,20,20,20]
VecEnd_z = [0,20,18 ,16,14,12,10,8,6,4,2]
for i in range(len(VecEnd_x)):
    axes.scatter3D(VecEnd_x[i], VecEnd_y[i], VecEnd_z[i], c=10)
    axes.plot([VecStart_x[i], VecEnd_x[i]], [VecStart_y[i],
                                           VecEnd_y[i]], zs=[VecStart_z[i], VecEnd_z[i]])
plot.show()
