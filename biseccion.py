import math

def biseccion(func, a, b, error, max_iter):
    # Verifica si la función cambia de signo en el intervalo [a, b]
    if func(a) * func(b) >= 0:
        raise ValueError("La función debe cambiar de signo en el intervalo dado")

    iteracion = 0
    # Aplica el método de bisección hasta alcanzar el error deseado o el número máximo de iteraciones
    while (b - a) / 2 > error and iteracion < max_iter:
        # Calcula el punto medio del intervalo [a, b]
        c = (a + b) / 2

        # Si el valor de la función en el punto medio es exactamente cero, se ha encontrado la raíz
        if func(c) == 0.0:
            break

        # Actualiza los extremos del intervalo [a, b] basándose en el cambio de signo
        if func(c) * func(a) < 0:
            b = c
        else:
            a = c

        iteracion += 1

    # Devuelve la aproximación de la raíz encontrada usando el método de bisección
    return (a + b) / 2