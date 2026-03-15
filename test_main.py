import unittest
from io import StringIO
import sys

# Functions to test
def sum(a, b):
    print(a + b)

def multi(x, y):
    print(x * y)


class TestMathFunctions(unittest.TestCase):

    def test_sum(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        sum(10, 20)
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "30")

    def test_multi(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        multi(5, 2)
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "10")


if __name__ == "__main__":
    unittest.main()