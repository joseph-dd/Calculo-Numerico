import unittest
import math
from newton_raphson import newton_raphson

class TestNewtonRaphson(unittest.TestCase):

    def test_funcion_1(self):
        f = lambda x: math.exp(x) - 3*x**2
        x0 = 0.5
        err = 0.0003
        max_iter = 100
        resultado = newton_raphson( f, x0, err, max_iter)
        self.assertAlmostEqual(resultado, 0.9100075724887055, places=6)

    def test_funcion_2(self):
        f = lambda x: (x-2)**2 - math.log(x)
        x0 = 1.5
        err = 0.0004
        max_iter = 100
        resultado = newton_raphson( f, x0, err, max_iter)
        self.assertAlmostEqual(resultado, 1.4123911717276767, places=6)

if __name__ == '__main__':
    unittest.main()