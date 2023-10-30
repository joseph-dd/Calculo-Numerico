from math import log, e

def biseccion(func, a, b, error, max_iter):
    if func(a) * func(b) >= 0:
        raise ValueError("La función debe cambiar de signo en el intervalo dado")
    iter_count = 0
    while (b - a) / 2 > error and iter_count < max_iter:
        c = (a + b) / 2
        if func(c) == 0.0:
            break
        if func(c) * func(a) < 0:
            b = c
        else:
            a = c
        iter_count += 1
    return (a + b) / 2


def ValidarKW(mensaje, tipo):
    while True:
        try:
            valor = input(mensaje)
            if tipo == 'n':
                valor = int(valor)
                return valor
            elif tipo == 'f':
                valor = float(valor)
                return valor
            elif tipo == 'fx':
                valor = eval("lambda x: " + valor)
                return valor
        except ValueError: print("Ingrese una entrada valida...")

print("---------- Metodo de biseccion -----------")
f = ValidarKW("\nIngrese la funcion a evaluar: ",'fx')
a = ValidarKW("\nIngrese el primer intervalo: ", 'f')
b = ValidarKW("\nIngrese el segundo intervalo: ", 'f')
err = ValidarKW("\nIngrese margen de error relativo a calcular: ", 'f')
max_ite = ValidarKW("\nIngrese maximo de iteraciones: ",'n')
print("\n\nEl resultado es aproximadamente:",biseccion(f,a,b,err,max_ite))
