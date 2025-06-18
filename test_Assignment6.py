import unittest
from Assignment6 import Calculator

# Calculator Class unit tests

class TestAssignment6(unittest.TestCase):

    def test_CalcAdd(self):
        calc = Calculator()
        self.assertEqual(calc.add(1, 1), 2)

    def test_CalcSubtract(self):
        calc = Calculator()
        self.assertEqual(calc.subtract(1, 1), 0)

    def test_CalcMultiply(self):
        calc = Calculator()
        self.assertEqual(calc.multiply(2, 2), 4)

    def test_CalcDivide(self):
        calc = Calculator()
        self.assertEqual(calc.divide(4, 2), 2)
        
    def test_exponent(self):
        calc = Calculator()
        self.assertEqual(calc.exponent(2, 3), 8)
      
    def test_divide_by_zero(self):
        calc = Calculator()
        with self.assertRaises(ValueError):
            calc.divide(1, 0)
   

if __name__ == '__main__':
    unittest.main()