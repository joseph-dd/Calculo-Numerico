import unittest
import math
from biseccion import biseccion  # Importa la función biseccion
from newton import newton_raphson  # Importa la función newton_raphson
from riemann import riemann  # Importa la función riemann
from trapecio import trapecio  # Importa la función trapecio

class Tests(unittest.TestCase):

    def test_biseccion(self):
        # Define la función, el intervalo [a, b], el error y el número máximo de iteraciones
        f = lambda x: x**2 - 4
        a, b = 0, 3
        err = 1e-10
        max_iter = 1000

        # Aplica el método de bisección y verifica el resultado
        resultado = biseccion(f, a, b, err, max_iter)
        self.assertAlmostEqual(resultado, 2.0, places=10)
    
    def test_newton(self):
        # Define la función, el punto inicial, el error y el número máximo de iteraciones
        f = lambda x: math.exp(x) - 3*x**2
        x0 = 0.5
        err = 0.0003
        max_iter = 100

        # Aplica el método de Newton-Raphson y verifica el resultado
        resultado = newton_raphson(f, x0, err, max_iter)
        self.assertAlmostEqual(resultado, 0.9100075724887055, places=6)
    
    def test_riemann(self):
        # Define la función, el intervalo [a, b], y el número de subintervalos
        f = lambda x: ((3*x) / (x**2 + 1))
        a, b = 1, 2
        n = 4

        # Aplica la regla de Riemann y verifica el resultado 
        resultado = riemann(f, a, b, n)
        self.assertAlmostEqual(resultado, 1.4100844277673545, places=10)
    
    def test_trapecio(self):
        # Define la función, el intervalo [a, b], y el número de subintervalos
        f = lambda x: x * ((x**2 + 1)**0.5)
        a, b = 0, 1
        n = 4

        # Aplica la regla del trapecio y verifica el resultado 
        resultado = trapecio(f, a, b, n)
        self.assertAlmostEqual(resultado, 0.6153294692906497, places=10)

if __name__ == '__main__':
    unittest.main()