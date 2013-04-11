# Given an image represented by an NxN matrix, where each pixel in the image is
# four bytes, write a method to rotate the image by 90 degrees. Can you do this
# in place?

# Assuming each pixel is represented by a tuple; the matrix is a list of lists
# in row-major form; the rotation is clock-wise.

import unittest

def rotate(m):
  n = len(m[0])
  cur_replacement_index = 1
    
  for r in m[:-1]:
    for i in range(cur_replacement_index, n):
      tmp = r[i]
      r[i] = m[i][cur_replacement_index - 1]
      m[i][cur_replacement_index - 1] = tmp

    cur_replacement_index += 1

  for r in m:
    r.reverse()

  return m

class RotateTest(unittest.TestCase):

  def test_rotate(self):
    input_m = [[1]]
    output_m = [[1]]
    self.assertEqual(rotate(input_m), output_m)

    input_m = [[1, 2], [3, 4]]
    output_m = [[3, 1], [4, 2]]
    self.assertEqual(rotate(input_m), output_m)

    input_m = [[1, 2, 3, 4],
               [12, 'a', 'b', 5],
               [11, 'd', 'c', 6],
               [10, 9, 8, 7]]
    output_m = [[10, 11, 12, 1],
                [9, 'd', 'a', 2],
                [8, 'c', 'b', 3],
                [7, 6, 5, 4]]
    self.assertEqual(rotate(input_m), output_m)
    
if __name__ == '__main__':
    unittest.main()

