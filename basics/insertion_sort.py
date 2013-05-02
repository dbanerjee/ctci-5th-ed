# Implementation of Insertion-Sort
#
# Nitin Punjabi
# nptoronto@yahoo.com
# https://github.com/nitinpunjabi

def insertion_sort(elems):
  max_idx = len(elems)
  for i in range(1, max_idx):
    j = i
    while elems[j] < elems[j - 1] and j is not 0:
      tmp = elems[j]
      elems[j] = elems[j - 1]
      elems[j - 1] = tmp
      j -= 1
