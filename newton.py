import math

def derivada(x, func):
    # Establece un valor pequeño para h, que se utiliza en la aproximación de la derivada
    h = 1e-10

    # Calcula la aproximación de la derivada en el punto x
    return (func(x + h) - func(x)) / h

def newton_raphson(func, x0, err, max_iter):
    # Inicializa el contador de iteraciones
    iteracion = 0

    # Itera hasta alcanzar el número máximo de iteraciones
    while iteracion < max_iter:
        # Calcula el valor de la función y su derivada en el punto actual x0
        fx = func(x0)
        f_prima = derivada(x0, func)

        # Verifica si la derivada es demasiado pequeña (posible división por cero)
        if abs(f_prima) < 1e-10:
            return None, False

        # Calcula el siguiente punto utilizando el método de Newton-Raphson
        x1 = x0 - fx / f_prima

        # Verifica si la aproximación es suficientemente precisa
        if abs(x1 - x0) < err:
            return x1

        # Actualiza x0 con el nuevo valor calculado
        x0 = x1
        iteracion += 1

    # Devuelve None si no se alcanzó la convergencia en el número máximo de iteraciones
    return None