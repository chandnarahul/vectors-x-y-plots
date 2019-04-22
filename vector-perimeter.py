import operations as op

# for perimeter
# we sum the distances of every pair of subsequent vectors in the list, 
# as well as the pair of the first and the last.
def perimeter(vectors):
    endMinusOne = len(vectors)-1
    distances = op.distance(vectors[0], vectors[endMinusOne])
    for i in range(endMinusOne):
        distances += op.distance(vectors[i], vectors[i+1])
    return distances

print(perimeter([(1,0),(1,1),(0,1),(0,0)]))