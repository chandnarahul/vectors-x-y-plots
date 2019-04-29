from math import sqrt


def length(v):
    return sqrt(v[0]**2 + v[1]**2)


def subtract(v1, v2):
    return (v1[0] - v2[0], v1[1] - v2[1])


def distance(v1, v2):
    return length(subtract(v1, v2))


def transformFrom(v1, toV2):
    return (v1[0]+toV2[0], v1[1]+toV2[1])
