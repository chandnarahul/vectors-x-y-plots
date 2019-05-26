from mpl_toolkits import mplot3d
import matplotlib.pyplot as plot

figure = plot.figure()
axes = plot.axes(projection='3d')

axes.scatter3D(10, 10, 10, c=10)

plot.show()
