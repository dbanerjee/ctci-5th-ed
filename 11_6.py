# 11.6 Given an MxN matrix in which each row and each column is sorted in
# ascending order, write a method to find an element.

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

