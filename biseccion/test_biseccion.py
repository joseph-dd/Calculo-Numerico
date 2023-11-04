import unittest
import math
from biseccion import biseccion

class TestBiseccion(unittest.TestCase):
    
    def test_funcion_1(self):
        f = lambda x: x**2 - 4
        a, b = 0, 3
        err = 1e-10
        max_iter = 1000
        resultado = biseccion(f, a, b, err, max_iter)
        self.assertAlmostEqual(resultado, 2.0, places=10)
    
    def test_funcion_2(self):
        f = lambda x: (x - 2)**2 - math.log(x)
        a, b = 1, 2
        err = 0.04
        max_iter = 1000
        resultado = biseccion(f, a, b, err, max_iter)
        self.assertAlmostEqual(resultado, 1.40625, places=10)

if __name__ == '__main__':
    unittest.main()