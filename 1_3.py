# Given two strings, write a method to decide if one is a permutation of
# another.

import unittest

def is_permutation_sort(s1, s2):
  return sorted(s1) == sorted(s2)

# Works on only all lower-case or all upper-case strings.
def is_permutation_ord(s1, s2):
  s1_val = reduce(lambda x, y: x + y, map(lambda x: ord(x), s1))
  s2_val = reduce(lambda x, y: x + y, map(lambda x: ord(x), s2))
  return s1_val == s2_val

class PermutationTest(unittest.TestCase):

  def test_permutation_sort(self):
    self.assertEqual(is_permutation_sort("racecar", "carrace"), True)
    self.assertEqual(is_permutation_sort("racecar", "car race"), False)
    self.assertEqual(is_permutation_sort("Racecar", "Carrace"), False)

  def test_permutation_ord(self):
    self.assertEqual(is_permutation_ord("racecar", "carrace"), True)
    self.assertEqual(is_permutation_ord("racecar", "car race"), False)

if __name__ == '__main__':
    unittest.main()