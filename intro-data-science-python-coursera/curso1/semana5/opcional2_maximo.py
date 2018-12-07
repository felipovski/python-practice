def maximo(x, y, z):

    if x < y and z < y:
        return y
    if x < z and y < z:
        return z
    return x
