# Solution to Exercise 2.1 from Cracking the Coding Interview, 5th Edition
# Nitin Punjabi
# nptoronto@yahoo.com
# https://github.com/nitinpunjabi

import linked_list as lst

def remove_dups(lst):
  elems = set()
  elems.add(lst.head.item)
  pred_node = lst.head
  
  while pred_node.next:
    if pred_node.next.item in elems:
      if lst.tail == pred_node.next:
        lst.tail = pred_node
        pred_node.next = None
      else:
        pred_node.next = pred_node.next.next

      lst.length -= 1
    
    else:
      elems.add(pred_node.next.item)
      pred_node = pred_node.next

  return lst.enumerate()


