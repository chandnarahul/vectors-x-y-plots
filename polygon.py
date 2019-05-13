from coordinates import to_cartesian_in_radian
from coordinates import to_polar
from math import pi
from matplotlib import pyplot as plot


def polygon(sides):
    startingDegree = 360 / sides
    for i in range(0, sides):
        v1 = to_cartesian_in_radian((startingDegree*i*pi/180, 1))
        plot.scatter(v1[0], v1[1], s=10)
    plot.show()

polygon(7)