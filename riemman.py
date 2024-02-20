import math

def riemman(func, a, b, n):
    h = (b - a) / n
    acum = 0.0
    x = a
    for i in range (n):
        acum += func(x) * h
        x += h
    return acum