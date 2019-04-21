from math import sqrt

def length(v):
    return sqrt(v[0]**2 + v[1]**2)

def subtract(v1,v2):
    return (v1[0] - v2[0], v1[1] - v2[1])

def distance(v1,v2):
    return length(subtract(v1,v2))

# for perimeter
# we sum the distances of every pair of subsequent vectors in the list, 
# as well as the pair of the first and the last.
def perimeter(vectors):
    endMinusOne = len(vectors)-1
    distances = distance(vectors[0], vectors[endMinusOne])
    for i in range(endMinusOne):
        distances += distance(vectors[i], vectors[i+1])
    return distances

print(perimeter([(1,0),(1,1),(0,1),(0,0)]))