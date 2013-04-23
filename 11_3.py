# 11.3 Given a sorted array of n integers that has been rotated an unknown
# number of times, write code to find an element in the array. You may assume
# that the array was originally sorted in increasing order.
# Example:
# Input: Find 5 in [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14].
# Output: 8 (the index of 5 in the array)

def _search_rotated(elems, left, right, target):
  m = (left + right) / 2
  if elems[m] is target:
    return m

  if (elems[m] > target and elems[right] >= target and elems[right] <=\
      elems[m]) or (elems[m] < target and elems[right] >= target):
    return _search_rotated(elems, m + 1, right, target)
  elif (elems[m] < target and elems[left] <= target and elems[left] >=\
        elems[m]) or (elems[m] > target and elems[left] <= target):
    return _search_rotated(elems, left, m - 1, target)
  else:
    return False

def search_related(elems, target):
  return _search_rotated(elems, 0, len(elems) - 1, target)