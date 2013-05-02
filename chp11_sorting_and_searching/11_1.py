# Solution to Exercise 11.1 from Cracking the Coding Interview, 5th Edition
# Nitin Punjabi
# nptoronto@yahoo.com
# https://github.com/nitinpunjabi

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
