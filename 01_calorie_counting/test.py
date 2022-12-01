import unittest
from lib import ex1, ex2

input = './test_input.txt'

class Tests(unittest.TestCase):
    def test_ex1(self):
        self.assertEqual(ex1(input), 24000)

    def test_ex2(self):
        self.assertEqual(ex2(input), 45000)

if __name__ == '__main__':
    unittest.main()
