# Solution to Exercise 1.6 from Cracking the Coding Interview, 5th Edition
# Nitin Punjabi
# nptoronto@yahoo.com
# https://github.com/nitinpunjabi
#
# Assumptions:
# - Matrix is NxN and represented as a list of lists
# - Rotation is clockwise

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
