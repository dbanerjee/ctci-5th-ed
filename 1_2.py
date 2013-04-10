# Implement a function void reverse (char* str) in C or C++ which reverses a
# null-terminated string.

import unittest

def reverse_s(s):
  l = []
  for i in range(len(s) - 1, -1, -1):
    l.append(s[i])

  return "".join(l)

class UniqueStringTest(unittest.TestCase):

  def test_reverse_string(self):
    self.assertEqual(reverse_s(" "), " ")
    self.assertEqual(reverse_s("t"), "t")
    self.assertEqual(reverse_s("this"), "siht")
    self.assertEqual(reverse_s("this "), " siht")
    self.assertEqual(reverse_s("this is"), "si siht")
    self.assertEqual(reverse_s("this  is it"), "ti si  siht")

if __name__ == '__main__':
    unittest.main()
