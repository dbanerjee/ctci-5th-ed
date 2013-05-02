# Solution to Exercise 11.6 from Cracking the Coding Interview, 5th Edition
# Nitin Punjabi
# nptoronto@yahoo.com
# https://github.com/nitinpunjabi

def search_matrix(mat, target):
  top = 0
  right = len(mat[0]) - 1 
  bottom = len(mat) - 1

  while top <= bottom and right >= 0:
    cur = mat[top][right]
    if cur is target:
      return (top, right)

    if cur < target:
      top += 1
    else:
      right -= 1

  return None

