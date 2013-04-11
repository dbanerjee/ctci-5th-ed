# Write an algorithm such that if an element in an MxN matrix is 0, its entire
# row and column are set to 0.

import unittest

def zero_out(m):
  rows = set()
  cols = set()
  row_count = len(m)
  col_count = len(m[0])

  for i in range(row_count):
    for j in range(col_count):
      if m[i][j] == 0:
        rows.add(i)
        cols.add(j)
  
  for row in rows:
    m[row] = map(lambda x: 0, m[row])

  for col in cols:
    for i in range(row_count):
      m[i][col] = 0

  return m

class ZeroOutTest(unittest.TestCase):

  def test_zero_out(self):
    input_m = [[1]]
    output_m = [[1]]
    self.assertEqual(zero_out(input_m), output_m)

    input_m = [[1, 0]]
    output_m = [[0, 0]]
    self.assertEqual(zero_out(input_m), output_m)

    input_m = [[1, 1]]
    output_m = [[1, 1]]
    self.assertEqual(zero_out(input_m), output_m)

    input_m = [[1, 1],
               [1, 0]]
    output_m = [[1, 0],
                [0, 0]]
    self.assertEqual(zero_out(input_m), output_m)    

    input_m = [[1, 1],
               [0, 0]]
    output_m = [[0, 0],
                [0, 0]]
    self.assertEqual(zero_out(input_m), output_m)  

    input_m = [[1, 1],
               [1, 1]]
    output_m = [[1, 1],
                [1, 1]]
    self.assertEqual(zero_out(input_m), output_m)    

    input_m = [[1, 1, 1, 1],
               [0, 1, 1, 0]]
    output_m = [[0, 1, 1, 0],
                [0, 0, 0, 0]]
    self.assertEqual(zero_out(input_m), output_m)  

    
if __name__ == '__main__':
    unittest.main()
