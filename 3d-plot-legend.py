from mpl_toolkits import mplot3d
import matplotlib.pyplot as plot

figure = plot.figure()
axes = plot.axes(projection='3d')

# Stablishing the plots of our legend labels
blue_proxy = plot.Rectangle((0, 0), 1, 1, fc='b')
red_proxy = plot.Rectangle((0, 0), 1, 1, fc='r')
green_proxy = plot.Rectangle((0, 0), 1, 1, fc='g')
black_proxy = plot.Line2D([0], [0], linestyle="none", marker='o',
                          alpha=0.6, markersize=10, markerfacecolor='black')

# Drawing Our Legend
axes.legend([blue_proxy, red_proxy, green_proxy, black_proxy], [r'$x+y-z=1$',
                                                                r'$x-y+z=1$', r'$-x+y+z=1$', r'$Sol.\; (1,1,1)$'], numpoints=1, loc='upper left')

plot.show()
