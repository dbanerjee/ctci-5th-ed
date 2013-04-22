# Implementation of bubble-sort.

def bubble_sort(elems):
  max_idx = len(elems) - 1
  for i in range(max_idx, -1, -1):
    cur = 0
    while cur is not i:
      if elems[cur] > elems[cur + 1]:
        tmp = elems[cur]
        elems[cur] = elems[cur + 1]
        elems[cur +  1] = tmp
      cur += 1


