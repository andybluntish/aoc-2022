import unittest
from lib import find_marker, ex1, ex2

test_input = './input_test.txt'
real_input = './input.txt'

class Tests(unittest.TestCase):
    # Part 1
    def test_ex1_test_input(self):
        self.assertEqual(ex1(test_input), 7)
        self.assertEqual(find_marker("bvwbjplbgvbhsrlpgdmjqwftvncz", 4), 5)
        self.assertEqual(find_marker("nppdvjthqldpwncqszvftbrmjlhg", 4), 6)
        self.assertEqual(find_marker("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 4), 10)
        self.assertEqual(find_marker("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 4), 11)

    def test_ex1_real_input(self):
        self.assertEqual(ex1(real_input), 1779)

    # Part 2
    def test_ex2_test_input(self):
        self.assertEqual(ex2(test_input), 19)
        self.assertEqual(find_marker("bvwbjplbgvbhsrlpgdmjqwftvncz", 14), 23)
        self.assertEqual(find_marker("nppdvjthqldpwncqszvftbrmjlhg", 14), 23)
        self.assertEqual(find_marker("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 14), 29)
        self.assertEqual(find_marker("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 14), 26)

    def test_ex2_real_input(self):
        self.assertEqual(ex2(real_input), 2635)

if __name__ == '__main__':
    unittest.main()
