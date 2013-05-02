# Solution to Exercise 11.3 from Cracking the Coding Interview, 5th Edition
# Nitin Punjabi
# nptoronto@yahoo.com
# https://github.com/nitinpunjabi

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

def search_rotated(elems, target):
  return _search_rotated(elems, 0, len(elems) - 1, target)