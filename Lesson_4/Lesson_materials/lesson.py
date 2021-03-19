# pip3 install unittest
# python3 -m unittest lesson.py

import unittest


def sum_sq(i, j):
    return i * i + j * j


class SumSqTestCase(unittest.TestCase):
    pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_equal(self):
        self.assertEqual(sum_sq(2, 3), 13)


if __name__ == '__main__':
    unittest.main()