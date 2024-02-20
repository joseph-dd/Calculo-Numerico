import math

def biseccion(func, a, b, error, max_iter):
    if func(a) * func(b) >= 0:
        raise ValueError("La función debe cambiar de signo en el intervalo dado")
    iteracion = 0
    while (b - a) / 2 > error and iteracion < max_iter:
        c = (a + b) / 2
        if func(c) == 0.0:
            break
        if func(c) * func(a) < 0:
            b = c
        else:
            a = c
        iteracion += 1
    return (a + b) / 2