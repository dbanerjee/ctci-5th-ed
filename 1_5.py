# Implement a method to perform basic string compression using the counts of
# repeated characters. For example, the string "aabcccccaaa" should return
# a2b1c5a3. If the "compressed" string would not become smaller than the
# original string, your method should return the original string.

import unittest

def compress(s):
  if not s:
    return s

  count = 0
  char_reps = []
  last_char = s[0]

  for c in s:
    if c != last_char:
      char_reps.append("".join([last_char, str(count)]))
      count = 0

    count += 1
    last_char = c

  char_reps.append("".join([last_char, str(count)]))
  c_str = "".join(char_reps)
  if len(s) < len(c_str):
    return s
  else:
    return c_str

class CompressTest(unittest.TestCase):

  def test_compress(self):
    self.assertEqual(compress(""), "")
    self.assertEqual(compress(" "), " ")
    self.assertEqual(compress("a"), "a")
    self.assertEqual(compress("ab"), "ab")
    self.assertEqual(compress("a b"), "a b")
    self.assertEqual(compress("a b "), "a b ")
    self.assertEqual(compress("aabcccccaaa"), "a2b1c5a3")
    self.assertEqual(compress("aa bccccc aa"), "a2 1b1c5 1a2")

    
if __name__ == '__main__':
    unittest.main()