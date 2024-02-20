import math

def trapecio(func, a, b, n):
    h = (b - a) / n
    acum = 0.0
    x = a
    for i in range (n):
        acum += ((func(x) + func(x + h)) * h) / 2
        x += h
    return acum