def merge(left, right):
  a_list = []
  
  left_len = len(left) if left else 0
  right_len = len(right) if right else 0
  left_idx = 0
  right_idx = 0
  while left_idx < left_len and right_idx < right_len:
    if left[left_idx] <= right[right_idx]:
      a_list.append(left[left_idx])
      left_idx += 1
    else:
      a_list.append(right[right_idx])
      right_idx += 1

  if left_idx < left_len:
    a_list.extend(left[left_idx:])
  elif right_idx < right_len:
    a_list.extend(right[right_idx:])

  return a_list

def merge_sort(a_list):
  l = len(a_list)
  if l <= 1:
    return a_list

  m = l / 2
  left = merge_sort(a_list[:m])
  right = merge_sort(a_list[m:])
  return merge(left, right)
