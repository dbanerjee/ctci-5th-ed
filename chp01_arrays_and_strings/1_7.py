# Solution to Exercise 1.7 from Cracking the Coding Interview, 5th Edition
# Nitin Punjabi
# nptoronto@yahoo.com
# https://github.com/nitinpunjabi
#
# Assumptions:
# - Matrix is MxN and represented as a list of lists.

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
