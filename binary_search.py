# Implementation of binary search

def _binary_search(elems, left, right, target):
  if left >= right:
    return False

  m = (left + right) / 2
  if elems[m] is target:
    return True

  if elems[m] > target:
    return _binary_search(elems, left, m - 1, target)
  else:
    return _binary_search(elems, m + 1, right, target)

def binary_search(elems, target):
  return _binary_search(elems, 0, len(elems), target)

