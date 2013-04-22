# Implementation of selection-sort

def selection_sort(elems):
  max_idx = len(elems)
  for i in range(max_idx):
    cur_max = i
    j = i
    while j is not max_idx:
      if elems[j] < elems[cur_max]:
        cur_max = j
      j += 1
    if cur_max is not i:
      tmp = elems[i]
      elems[i] = elems[cur_max]
      elems[cur_max] = tmp

