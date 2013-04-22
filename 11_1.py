# 11.1 You are given two sorted arrays, A and B, where A has a large enough
# buffer at the end to hold B. Write a method to merge B into A in sorted order.

def merge_sorted_arrays(a_list, b_list):
  master_idx = len(a_list) - 1
  a_idx = 0
  while True:
    if a_list[a_idx + 1] is None:
      break
    a_idx += 1  
  b_idx = len(b_list) - 1

  while a_idx >= 0 and b_idx >= 0:
    if a_list[a_idx] > b_list[b_idx]:
      a_list[master_idx] = a_list[a_idx]
      a_idx -= 1
    else:
      a_list[master_idx] = b_list[b_idx]
      b_idx -= 1
    master_idx -= 1

  while b_idx >= 0:
    a_list[master_idx] = b_list[b_idx]
    b_idx -= 1
    master_idx -= 1


a = [2, 4, 6, 8, 10, 12, 14, 16, None, None, None, None]
b = [1, 3, 5, 7]

