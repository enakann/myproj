from calc import Calculator
import unittest


class TestCalculator(unittest.TestCase):

    def setUp(cls):
        cls.calc=Calculator(2,1)

    def test_add(self):
        self.assertEqual(self.calc.add(),3)

    def test_sub(self):
        self.assertEqual(self.calc.sub(),1)



if __name__ == '__main__':
    unittest.main()
