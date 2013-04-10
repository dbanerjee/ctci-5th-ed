# Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures.

import unittest

# Solution using dict.
def unique_chars_dict(s):
  chars = {}
  for c in s:
    if c != ' ':
      if c in chars:
        return False
      else:
        chars[c] = 1

  return True

# Solution using no additional data structures.
def unique_chars_sort(s):
  sorted_s = sorted(s)
  for i in range(1, len(sorted_s)):
    if sorted_s[i] != ' ':
      if sorted_s[i] == sorted_s[i - 1]:
        return False

  return True

class UniqueCharsTest(unittest.TestCase):

  def test_unique_chars_dict(self):
    self.assertEqual(unique_chars_dict("a"), True)
    self.assertEqual(unique_chars_dict("aa"),False)
    self.assertEqual(unique_chars_dict("a "),True)
    self.assertEqual(unique_chars_dict("a  "),True)
    self.assertEqual(unique_chars_dict("ab"),True)
    self.assertEqual(unique_chars_dict("aA"),True)
    self.assertEqual(unique_chars_dict("ab cd ef"),True)
    self.assertEqual(unique_chars_dict("a  a"), False)
    self.assertEqual(unique_chars_dict(" "), True)
   
  def test_unique_chars_sort(self):
    self.assertEqual(unique_chars_sort("a"), True)
    self.assertEqual(unique_chars_sort("aa"),False)
    self.assertEqual(unique_chars_sort("a "),True)
    self.assertEqual(unique_chars_sort("a  "),True)
    self.assertEqual(unique_chars_sort("ab"),True)
    self.assertEqual(unique_chars_sort("aA"),True)
    self.assertEqual(unique_chars_sort("ab cd ef"),True)
    self.assertEqual(unique_chars_sort("a  a"), False)
    self.assertEqual(unique_chars_sort(" "), True)

if __name__ == '__main__':
    unittest.main()




