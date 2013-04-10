# Write a method to replace all space characters in a string with '%20'.

import unittest

def replace_char(s, trgt, new_char):
  l = []
  for c in s:
    if c == " ":
      l.append('%20')
    else:
      l.append(c)

  return "".join(l)

class UniqueStringTest(unittest.TestCase):

  def test_replace_char(self):
    self.assertEqual(replace_char("", " ", "%20"), "")
    self.assertEqual(replace_char(" ", " ", "%20"), "%20")
    self.assertEqual(replace_char("t", " ", "%20"), "t")
    self.assertEqual(replace_char("t h", " ", "%20"), "t%20h")
    self.assertEqual(replace_char("t h  i   s", " ", "%20"),
                      "t%20h%20%20i%20%20%20s")

if __name__ == '__main__':
    unittest.main()