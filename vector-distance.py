import operations as op

for n in range(-12,15):
    for m in range(-14, 13):
        if op.distance((n,m), (1,-1)) == 13 and n > m > 0:
            print((n,m))


print(op.length((-1.34, 2.68)))
