from matplotlib import pyplot as plot
from coordinates import to_polar
from operations import transformFrom
from coordinates import to_cartesian
from math import pi


def plotPoints(dino_vectors, scale_x, scale_y):
    dino_length = len(dino_vectors)
    dino_sub_length = dino_length - 1

    for i in range(dino_length):
        plot.scatter(dino_vectors[i][0] + scale_x,
                     dino_vectors[i][1] + scale_y, s=0.1)

    plot.plot([dino_vectors[0][0] + scale_x, dino_vectors[dino_sub_length][0] + scale_x],
              [dino_vectors[0][1] + scale_y, dino_vectors[dino_sub_length][1] + scale_y])
    for i in range(dino_sub_length):
        plot.plot([dino_vectors[i][0] + scale_x, dino_vectors[i+1][0] + scale_x],
                  [dino_vectors[i][1] + scale_y, dino_vectors[i+1][1] + scale_y])


dino_vectors = [
    (6, 4), (3, 1), (1, 2),
    (-1, 5), (-2, 5), (-3, 4),
    (-4, 4), (-5, 3), (-5, 2),
    (-2, 2), (-5, 1), (-4, 0),
    (-2, 1), (-1, 0), (0, -3),
    (-1, -4), (1, -4), (2, -3),
    (1, -2), (3, -1), (5, 1)
]

figure = plot.figure()
axes = figure.add_subplot(1, 1, 1)
axes.spines['left'].set_position('center')
axes.spines['bottom'].set_position('center')

rotation_angle = pi/4
for i in range(len(dino_vectors)):
    dino_polar = to_polar(dino_vectors[i])
    dino_rotated_polar = (dino_polar[0] + rotation_angle, dino_polar[1])
    dino_vectors[i] = to_cartesian(dino_rotated_polar)

plotPoints(dino_vectors, 0, 0)
for i in 10, 20, 30, 40, 50:
    plotPoints(dino_vectors, 0, i)
    plotPoints(dino_vectors, 0, -i)
    plotPoints(dino_vectors, i, 0)
    plotPoints(dino_vectors, -i, 0)
    plotPoints(dino_vectors, i, i)
    plotPoints(dino_vectors, -i, -i)
    plotPoints(dino_vectors, -i, i)
    plotPoints(dino_vectors, i, -i)

for i in range(len(dino_vectors)):
    dino_vectors[i] = transformFrom(dino_vectors[i], (8, 8))

plotPoints(dino_vectors, 0, 0)
for i in 10, 20, 30, 40, 50:
    plotPoints(dino_vectors, 0, i)
    plotPoints(dino_vectors, 0, -i)
    plotPoints(dino_vectors, i, 0)
    plotPoints(dino_vectors, -i, 0)
    plotPoints(dino_vectors, i, i)
    plotPoints(dino_vectors, -i, -i)
    plotPoints(dino_vectors, -i, i)
    plotPoints(dino_vectors, i, -i)

plot.show()
