import math

def trapecio(func, a, b, n):
    # Calcula el ancho de cada subintervalo
    h = (b - a) / n

    # Inicializa la variable acumuladora para la suma de áreas
    acum = 0.0

    # Inicializa la variable x con el límite inferior del intervalo
    x = a

    # Itera a través de los subintervalos y aplica la regla del trapecio
    for i in range(n):
        # Calcula el área del trapecio y lo agrega a la acumuladora
        acum += ((func(x) + func(x + h)) * h) / 2

        # Actualiza la posición de x para el siguiente subintervalo
        x += h

    # Devuelve la suma acumulada de las áreas bajo la curva
    return acum