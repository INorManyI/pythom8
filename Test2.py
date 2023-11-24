import unittest
from math import inf, pi
from main2 import abs
from main2 import factorial
from main2 import cos
from main2 import sin
from main2 import ln
from main2 import func

class TestAbs(unittest.TestCase):
    def test_abs1(self):
        inputs = [1, 2, 3, 4]
        expectedOutputs = [1, 2, 3, 4]
        for i in range(len(inputs)):
            self.assertEqual(abs(inputs[i]), expectedOutputs[i])

    def test_abs2(self):
        inputs = [-1, -2, -3, -4]
        expectedOutputs = [1, 2, 3, 4]
        for i in range(len(inputs)):
            self.assertEqual(abs(inputs[i]), expectedOutputs[i])

class TestFactorial(unittest.TestCase):
    def test_factorial1(self):
        inputs = [0, 1, 2, 3, 4]
        expectedOutputs = [1, 1, 2, 6, 24]
        for i in range(len(inputs)):
            self.assertEqual(factorial(inputs[i]), expectedOutputs[i])

class TestFactorial2(unittest.TestCase):
    def test_factorial(self):
        with self.assertRaises(Exception) as assert_error:
            self.assertEqual(factorial(-1), 1)

class TestCos(unittest.TestCase):
    def test_cos(self):
        inputs = [pi/2, 0.5, 1, 2]
        expectedOutputs = [0, 0.8775826, 0.540302305868139, -0.4161468365471423869975682]
        for i in range(len(inputs)):
            self.assertAlmostEqual(cos(inputs[i]), expectedOutputs[i], places=3)

class TestSin(unittest.TestCase):
    def test_sin1(self):
        inputs          = [pi/2, 0.5,      1,        2]
        expectedOutputs = [1,    0.479426, 0.841470, 0.909297]
        for i in range(len(inputs)):
            self.assertAlmostEqual(sin(inputs[i]), expectedOutputs[i], places=3)

class TestLn(unittest.TestCase):
    def test_ln1(self):
        inputs          = [pi/2,       0.5,       1, 2]
        expectedOutputs = [0.45158,    -0.693147, 0, 0.6931]
        for i in range(len(inputs)):
            self.assertAlmostEqual(ln(inputs[i]), expectedOutputs[i], places=3)

class TestLn2(unittest.TestCase):
    def test_ln2(self):
        with self.assertRaises(Exception) as assert_error:
            self.assertEqual(ln(-0.5), 1)

class TestIntegrLnCos(unittest.TestCase):
    def test_ln2(self):
        with self.assertRaises(Exception) as assert_error:
            self.assertEqual(ln(5), 1)
class TestSinCos(unittest.TestCase):
    def test_sincos(self):
        inputs = [pi / 2, 0.5, 1, 2]
        expectedOutputs = [1,1.3570086, 1.3817732, 0.4931505]
        for i in range(len(inputs)):
            self.assertAlmostEqual(sin(inputs[i]) + cos(inputs[i]), expectedOutputs[i], places=3)

class TestLnCos(unittest.TestCase):
    def test_ln_cos(self):
        inputs = [pi / 2, 0.5, 1, 2]
        expectedOutputs = [0.4515827,-1.570729, -0.5403023, 1.109294]
        for i in range(len(inputs)):
            self.assertAlmostEqual(ln(inputs[i]) - cos(inputs[i]), expectedOutputs[i], places=3)

class Testfunc(unittest.TestCase):
    def test_func1(self):
        self.assertEqual(func(-0.5), -1.9577488602923039)
class Testfunc2(unittest.TestCase):
    def test_func1(self):
        self.assertEqual(func(0), inf)


class TestLnAbs(unittest.TestCase):
    def test_lnAbs(self):
        inputs          = [pi/2,       -0.5,       -1, -2]
        expectedOutputs = [0.45158,    -0.693147, 0, 0.6931]
        for i in range(len(inputs)):
            self.assertAlmostEqual(ln(abs(inputs[i])), expectedOutputs[i], places=3)

if __name__ == "__main__":
    unittest.main()
