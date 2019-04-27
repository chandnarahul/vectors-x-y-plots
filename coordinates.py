from math import atan2
from math import cos
from math import sin
from operations import length


def angle(vector):
    y, x = vector[1], vector[0]
    return atan2(y, x)


def to_polar(cartesian_vector):
    return angle(cartesian_vector), length(cartesian_vector)


def to_cartesian(polar_vector):
    vector_length = polar_vector[1]
    return (vector_length * cos(polar_vector[0])), (vector_length * sin(polar_vector[0]))
