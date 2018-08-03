def shapeArea(n):
    t = 4
    x = 1
    for i in range(1,n):
        x = t + x
        t = t + 4
    return x
