import unittest
from lib import ex1, ex2

test_input = './input_test.txt'
real_input = './input.txt'

class Tests(unittest.TestCase):
    # Part 1
    def test_ex1_test_input(self):
        self.assertEqual(ex1(test_input, True), 24)

    #  def test_ex1_real_input(self):
        #  self.assertEqual(ex1(real_input), 5675)

    # Part 2
    #  def test_ex2_test_input(self):
        #  self.assertEqual(ex2(test_input), 140)

    #  def test_ex2_real_input(self):
        #  self.assertEqual(ex2(real_input), 20383)

if __name__ == '__main__':
    unittest.main()
