from math import sqrt

def length(v):
    return sqrt(v[0]**2 + v[1]**2)

def subtract(v1,v2):
    return (v1[0] - v2[0], v1[1] - v2[1])

def distance(v1,v2):
    return length(subtract(v1,v2))

for n in range(-12,15):
    for m in range(-14, 13):
        if distance((n,m), (1,-1)) == 13 and n > m > 0:
            print((n,m))