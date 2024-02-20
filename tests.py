import unittest
import math
from biseccion import biseccion
from newton import newton_raphson
from riemman import riemman
from trapecio import trapecio

class Tests(unittest.TestCase):

    def test_biseccion(self):
        f = lambda x: x**2 - 4
        a, b = 0, 3
        err = 1e-10
        max_iter = 1000
        resultado = biseccion(f, a, b, err, max_iter)
        self.assertAlmostEqual(resultado, 2.0, places=10)
    
    def test_newton(self):
            f = lambda x: math.exp(x) - 3*x**2
            x0 = 0.5
            err = 0.0003
            max_iter = 100
            resultado = newton_raphson( f, x0, err, max_iter)
            self.assertAlmostEqual(resultado, 0.9100075724887055, places=6)
    
    def test_riemman(self):
        f = lambda x: ((3*x) / (x**2 + 1))
        a, b = 1, 2
        n = 4
        resultado = riemman(f, a, b, n)
        self.assertAlmostEqual(resultado, 1.4100844277673545, places=10)
    
    def test_trapecio(self):
        f = lambda x: x * ((x**2 + 1)**0.5)
        a, b = 0, 1
        n = 4
        resultado = trapecio(f, a, b, n)
        self.assertAlmostEqual(resultado, 0.6153294692906497, places=10)

if __name__ == '__main__':
    unittest.main()