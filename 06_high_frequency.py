"""
High frequency
Given a list of integers nums, find the most frequently occurring
element and return the number of occurrence of that element.

For example, given the list [1, 4, 1, 7, 1, 7, 1, 1],
return 5 since the the element 1 appears 5 times.

Example 1
Input
nums = [1, 4, 1, 7, 1, 7, 1, 1]

Output
5

Example 2
Input
nums = [5, 5, 5, 5, 5, 5, 5]

Output
7

Example 3
Input
nums = [1, 2, 3, 4, 5, 6, 7]

Output
1
"""

import unittest

# Implement the below function and run this file
# Return the output, No need read input or print the ouput


def high_frequency(nums):
    pass


# DO NOT TOUCH THE BELOW CODE
class TestHighFrequency(unittest.TestCase):

    def test_01(self):
        self.assertEqual(high_frequency([1, 4, 1, 7, 1, 7, 1, 1]), 5)

    def test_02(self):
        self.assertEqual(high_frequency([5, 5, 5, 5, 5, 5, 5]), 7)

    def test_03(self):
        self.assertEqual(high_frequency([1, 2, 3, 4, 5, 6, 7]), 1)

    def test_04(self):
        self.assertEqual(high_frequency([18, 2, 16, 6, 5, 2, 19, 19, 13]), 2)

    def test_05(self):
        self.assertEqual(high_frequency([18, 3, 5, 2, 15, 19, 11, 7, 8, 4, 17, 5,
                                         18, 10, 1, 17, 9, 16, 6, 8, 9, 9, 7, 15, 13, 2, 13, 8, 2, 12]), 3)

    def test_06(self):
        self.assertEqual(high_frequency([9, 7, 2, 8, 7, 10, 1, 8, 2, 8, 4, 2, 6, 6, 6, 9, 10, 2, 1, 7, 3, 3,
                                         8, 2, 9, 6, 7, 9, 4, 9, 5, 6, 3, 7, 3, 8, 5, 10, 9, 9, 9, 6, 9, 6, 10, 9, 6, 1, 10, 4]), 10)

    def test_07(self):
        self.assertEqual(high_frequency([13, 21, 16, 12, 19, 18, 22, 14, 17, 15, 25, 15, 21, 15, 13, 12, 14, 17, 14, 22, 18, 11, 13, 23, 12, 17, 11, 13, 18, 19, 16, 14, 12, 16, 21, 17, 12, 10, 14, 17, 22, 13, 16, 17, 21, 20, 10, 13, 13, 21, 10, 20, 16, 21, 13, 10, 10, 18, 21,
                                         19, 24, 23, 21, 19, 25, 24, 10, 22, 11, 21, 16, 20, 13, 18, 12, 25, 10, 25, 22, 14, 16, 14, 22, 17, 22, 17, 14, 24, 25, 25, 23, 23, 22, 10, 14, 17, 10, 24, 10, 15, 11, 19, 15, 14, 17, 15, 22, 15, 14, 17, 22, 16, 16, 21, 25, 18, 18, 15, 22, 21, 11, 18, 22]), 12)


if __name__ == '__main__':
    unittest.main(verbosity=2)
