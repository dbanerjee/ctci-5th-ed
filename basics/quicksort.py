# Implementation of Quicksort
#
# Nitin Punjabi
# nptoronto@yahoo.com
# https://github.com/nitinpunjabi

def partition(elems, left, right):
  first = left
  piv = elems[first]

  while left <= right:

    while left <= right and elems[left] <= piv:
      left += 1
    while left <= right and elems[right] > piv:
      right -= 1

    if left < right:
      tmp = elems[left]
      elems[left] = elems[right]
      elems[right] = tmp
      print elems[left], elems[right]
  
  elems[first] = elems[right]
  elems[right] = piv
  return right

def _quicksort(elems, left, right):
  if left < right:
    new_piv_index = partition(elems, left, right)

    _quicksort(elems, left, new_piv_index - 1)
    _quicksort(elems, new_piv_index + 1, right)

def quicksort(elems):
  _quicksort(elems, 0, len(elems) - 1)
