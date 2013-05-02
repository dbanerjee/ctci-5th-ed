# Solution to Exercise 2.2 from Cracking the Coding Interview, 5th Edition
# Nitin Punjabi
# nptoronto@yahoo.com
# https://github.com/nitinpunjabi
#
# Assumptions:
# - k=1 represents the last element in the list

import linked_list as lst

def kth_to_last(k, lst):

  cur_pos = 0
  leading_node = lst.head
  trailing_node = lst.head

  while cur_pos != k:
    if leading_node:
      leading_node = leading_node.next
      cur_pos += 1
    else:
      return None

  while leading_node:
    leading_node = leading_node.next
    trailing_node = trailing_node.next

  return trailing_node.item
