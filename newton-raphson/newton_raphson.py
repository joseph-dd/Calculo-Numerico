import math

def derivada(x, func):
    h = 1e-10
    return (func(x + h) - func(x)) / h

def newton_raphson(func, x0, err, max_iter):
    iteracion = 0
    while iteracion < max_iter:
        fx = func(x0)
        f_prima = derivada(x0, func)

        if abs(f_prima) < 1e-10:
            return None, False

        x1 = x0 - fx / f_prima

        if abs(x1 - x0) < err:
            return x1

        x0 = x1
        iteracion += 1

    return None