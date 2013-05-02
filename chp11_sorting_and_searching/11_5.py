# Solution to Exercise 11.5 from Cracking the Coding Interview, 5th Edition
# Nitin Punjabi
# nptoronto@yahoo.com
# https://github.com/nitinpunjabi

def _find_string(elems, left, right, target):
  if left > right:
    return False

  m = (left + right) / 2
  if elems[m] is target:
    return m

  if elems[m]:
    if elems[m] > target:
      return _find_string(elems, left, m - 1, target)
    else:
      return _find_string(elems, m + 1, right, target)
  else:
    left_str = m
    right_str = m
    while left_str >= 0 and not elems[left_str]:
      left_str -= 1
    while right_str <= right and not elems[right_str]:
      right_str += 1

    if elems[left_str]:
      if elems[left_str] is target:
        return left_str
      elif elems[left_str] > target:
        return _find_string(elems, left, left_str - 1, target)
    
    if elems[right_str]:
      if elems[right_str] is target:
        return right_str
      elif elems[right_str] < target:
        return _find_string(elems, right_str + 1, right, target)

  return False

def find_string(elems, target):
  return _find_string(elems, 0, len(elems) - 1, target)
