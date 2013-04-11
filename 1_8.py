# Assume you have a method isSubstring which checks if one word is a substring
# of another. Given two strings, s1 and s2, write code to check if s2 is a
# rotation of s1 using only one call to isSubstring (e.g., "waterbottle is a
# rotation of "erbottlewat").

# This uses 'in' in place of isSubstring.

import unittest

def check_rotation(s1, s2):
  return s2 in s1 + s1

class RotationTest(unittest.TestCase):

  def test_rotation(self):
    self.assertEqual(check_rotation("erbottlewat", "waterbottle"), True)
    self.assertEqual(check_rotation("erbotlewat", "waterbottle"), False)
    
if __name__ == '__main__':
    unittest.main()

